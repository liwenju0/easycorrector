import easycorrector.ngram_model.load_model as load_model
import numpy as np
import easycorrector.common.common as common

model_name = "ngram_model"


def correct(text):
    lm = load_model.get_char_ngram_lm_model()
    maybe_errors = []
    if not text.strip():
        return maybe_errors

    ngram_avg_scores = []
    for n in [2, 3]:
        scores = []
        for i in range(len(text) - n + 1):
            word = text[i:i + n]
            score = lm.score(" ".join(word), bos=False, eos=False)
            scores.append(score)

        for _ in range(n - 1):
            scores.insert(0, scores[0])
            scores.append(scores[-1])
        avg_scores = [sum(scores[i:i + n]) / len(scores[i:i + n]) for i in range(len(text))]
        ngram_avg_scores.append(avg_scores)

    char_scores = list(np.average(np.array(ngram_avg_scores), axis=0))
    result = _compute_errors_and_correct(text, char_scores, lm)
    return result


def _compute_errors_and_correct(text, char_scores, lm, ratio=0.6745, threshold=3):
    """
    取疑似错字的位置，通过平均绝对离差（MAD）
    :param scores: np.array
    :param ratio: 正态分布表参数
    :param threshold: 阈值越小，得到疑似错别字越多
    :return: 全部疑似错误字的index: list
    """
    result = []
    scores = np.array(char_scores)
    if len(scores.shape) == 1:
        scores = scores[:, None]
    median = np.median(scores, axis=0)  # get median of all scores
    margin_median = np.abs(scores - median).flatten()  # deviation from the median
    # 平均绝对离差值
    med_abs_deviation = np.median(margin_median)
    if med_abs_deviation == 0:
        return result
    y_score = ratio * margin_median / med_abs_deviation
    # 打平
    scores = scores.flatten()
    maybe_error_indices = np.where((y_score > threshold) & (scores < median))
    # 取全部疑似错误字的index
    possible = list(maybe_error_indices[0])

    # 生成修改建议，目前留空
    result = []
    for idx in possible:
        replace_char = get_replace_char(text, idx, lm)
        if replace_char != text[idx]: # 添加一个修正项
            result.append(common.CorrectItem(start=idx, end=idx + 1, replace=replace_char))
        text = text[:idx] + replace_char + text[idx + 1:]
    return result

def get_replace_char(text, idx, lm):
    cur_char = text[idx]
    candidates = common.get_same_pinyin_or_same_stroke(cur_char)
    if cur_char not in candidates:
        candidates.add(cur_char)
    scores = {i: lm.score(" ".join(text[:idx] + i + text[idx + 1:])) for i in candidates}
    sorted_scores = sorted(scores.items(), key=lambda d: d[1], reverse=True)
    return sorted_scores[0][0]


