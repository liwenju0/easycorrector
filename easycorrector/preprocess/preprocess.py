from easycorrector.preprocess.full_half_width_convert import trans_char_number, trans_punc
from easycorrector.preprocess.illegal_char_filter import filter_out_illegal_char
from easycorrector.preprocess.simple_tradition_convert import t2s

def preprocess(text,
               need_t2s=True,
               need_trans_char_number=True,
               need_trans_punc=False,
               need_filter_out_illegal_char=True,
               need_lower=True):
    text = text.strip()
    if need_t2s:
        # 繁体转简体
        text = t2s(text)

    if need_trans_char_number:
        # 全角的英文字母、数字转半角
        text = trans_char_number(text, q2b=True)

    if need_trans_punc:
        # 英文标点转中文标点
        text = trans_punc(text, ch2en=False)
    if need_filter_out_illegal_char:
        # 过滤掉无效字符
        text = filter_out_illegal_char(text)

    if need_lower:
        text = text.lower()

    return text
