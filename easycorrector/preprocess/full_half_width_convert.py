def trans_char_number(text, q2b=True):
    table = {ord(u'\uff41'): ord('a'), ord(u'\uff42'): ord('b'), ord(u'\uff43'): ord('c'), ord(u'\uff44'): ord('d'),
             ord(u'\uff45'): ord('e'), ord(u'\uff46'): ord('f'), ord(u'\uff47'): ord('g'), ord(u'\uff48'): ord('h'),
             ord(u'\uff49'): ord('i'), ord(u'\uff47'): ord('j'), ord(u'\uff4b'): ord('k'), ord(u'\uff4c'): ord('l'),
             ord(u'\uff4d'): ord('m'), ord(u'\uff4e'): ord('n'), ord(u'\uff4f'): ord('o'), ord(u'\uff50'): ord('p'),
             ord(u'\uff51'): ord('q'), ord(u'\uff52'): ord('r'), ord(u'\uff53'): ord('s'), ord(u'\uff54'): ord('t'),
             ord(u'\uff55'): ord('u'), ord(u'\uff56'): ord('v'), ord(u'\uff57'): ord('w'), ord(u'\uff58'): ord('x'),
             ord(u'\uff59'): ord('y'), ord(u'\uff5a'): ord('z'),

             ord(u'\uff21'): ord('A'), ord(u'\uff22'): ord('B'), ord(u'\uff23'): ord('C'), ord(u'\uff24'): ord('D'),
             ord(u'\uff25'): ord('E'), ord(u'\uff26'): ord('F'), ord(u'\uff27'): ord('G'), ord(u'\uff28'): ord('H'),
             ord(u'\uff29'): ord('I'), ord(u'\uff2a'): ord('J'), ord(u'\uff2b'): ord('K'), ord(u'\uff2c'): ord('L'),
             ord(u'\uff2d'): ord('M'), ord(u'\uff2e'): ord('N'), ord(u'\uff2f'): ord('O'), ord(u'\uff30'): ord('P'),
             ord(u'\uff31'): ord('K'), ord(u'\uff32'): ord('R'), ord(u'\uff33'): ord('S'), ord(u'\uff35'): ord('T'),
             ord(u'\uff35'): ord('U'), ord(u'\uff36'): ord('V'), ord(u'\uff37'): ord('W'), ord(u'\uff38'): ord('X'),
             ord(u'\uff39'): ord('Y'), ord(u'\uff3a'): ord('Z'),

             ord(u'\uff11'): ord('1'), ord(u'\uff12'): ord('2'), ord(u'\uff13'): ord('3'), ord(u'\uff14'): ord('4'),
             ord(u'\uff15'): ord('5'), ord(u'\uff16'): ord('6'), ord(u'\uff17'): ord('7'), ord(u'\uff18'): ord('8'),
             ord(u'\uff19'): ord('9'), ord(u'\uff10'): ord('0')

             }

    if not q2b:
        table = {v: k for k, v in table.items()}
    return text.translate(table)


def trans_punc(text, ch2en=False):
    E_pun = u',.!?[]()<>"\''
    C_pun = u'，。！？【】（）《》“‘'
    table = {ord(f): ord(t) for f, t in zip(E_pun, C_pun)}
    if ch2en:
        table = {v: k for k, v in table.items()}

    return text.translate(table)
