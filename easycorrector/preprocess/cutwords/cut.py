from typing import Union, Iterable, List

import jieba
from pathlib import Path

jieba.load_userdict(str(Path(__file__).parent / "model_data/basic_words.txt"))
jieba.load_userdict(str(Path(__file__).parent / "model_data/sougou_domain_words.txt"))


def cut(text, cut_all=False, return_list=True) -> Union[List, Iterable]:
    if return_list:
        return list(jieba.cut(text, cut_all))
    else:
        return jieba.cut(text, cut_all)
