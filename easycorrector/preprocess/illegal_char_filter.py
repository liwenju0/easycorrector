'''
除了汉字、大小写英文字母、标点符号，其他都视为非法字符
'''
from string import punctuation as en_punctuation
from zhon.hanzi import punctuation as zh_punctuation

en_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"


def isHanPunc(char):
    return char in zh_punctuation


def isEnPunc(char):
    return char in en_punctuation


def isDigit(char):
    return char in digits


def isEnChar(char):
    return char in en_chars


def isHan(char):
    return "\u4e00" <= char <= "\u9fa5"


def isSpace(char):
    return char == " "


def isControl(char):
    return char == "\t" or char == "\n" or char == "\r"


def filter_out_illegal_char(text):
    res = ""
    for char in text:
        if isHanPunc(char) or \
                isEnPunc(char) or \
                isHan(char) or \
                isEnChar(char) or \
                isSpace(char) or \
                isControl(char) or \
                isDigit(char):
            res += char

    return res
