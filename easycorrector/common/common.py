from pathlib import Path
import os

same_pinyin_path = str(Path(__file__).parent / "model_data/same_pinyin.txt")
same_stroke_path = str(Path(__file__).parent / "model_data/same_stroke.txt")


class CorrectItem(object):
    '''
    start==end    表示增
    replace == "" 表示删
    其他           表示改
     '''

    def __init__(self, start, end, replace="", type="拼写错误"):
        self.start = start
        self.end = end
        self.replace = replace
        self.type = type

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def load_same_pinyin(path, sep='\t'):
    """
    加载同音字
    :param path:
    :param sep:
    :return:
    """
    result = dict()
    if not os.path.exists(path):
        print("file not exists:" + path)
        return result
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue
            parts = line.split(sep)
            if parts and len(parts) > 2:
                key_char = parts[0]
                same_pron_same_tone = set(list(parts[1]))
                same_pron_diff_tone = set(list(parts[2]))
                value = same_pron_same_tone.union(same_pron_diff_tone)
                if key_char and value:
                    result[key_char] = value
    return result


def load_same_stroke(path, sep='\t'):
    """
    加载形似字
    :param path:
    :param sep:
    :return:
    """
    result = dict()
    if not os.path.exists(path):
        print("file not exists:" + path)
        return result
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue
            parts = line.split(sep)
            if parts and len(parts) > 1:
                for i, c in enumerate(parts):
                    exist = result.get(c, set())
                    current = set(list(parts[:i] + parts[i + 1:]))
                    result[c] = exist.union(current)
    return result


same_pinyin = load_same_pinyin(same_pinyin_path)
same_stroke = load_same_stroke(same_stroke_path)


def get_same_pinyin_or_same_stroke(char):
    return same_stroke.get(char, set()).union(same_pinyin.get(char, set()))
