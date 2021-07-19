import opencc

s2t_converter = opencc.OpenCC('s2t.json')
t2s_converter = opencc.OpenCC('t2s.json')


def s2t(text: str) -> str:
    return s2t_converter.convert(text)


def t2s(text: str) -> str:
    return t2s_converter.convert(text)
