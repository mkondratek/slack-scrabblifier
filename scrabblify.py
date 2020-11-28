#!/usr/bin/python

import string
import sys

polish_with_acute_to_base={'ć': "c", 'ń': "n", 'ó': "o", 'ś': "s", 'ź': "z"}
polish_with_ogonek_to_base={'ą': "a", 'ę': "e", 'ć': "c"}
polish_with_overdot_to_base={'ż': "z"}
polish_with_stroke_to_base={'ł': "l"}
polish=dict()
polish.update(polish_with_acute_to_base)
polish.update(polish_with_ogonek_to_base)
polish.update(polish_with_overdot_to_base)
polish.update(polish_with_stroke_to_base)


eszett={'ß': "eszett"}
umlauts={'ä': "a", 'ü': "u", 'ö': "o"}
german=dict()
german.update(eszett)
german.update(umlauts)

scrabble_name_prefix=":scrabble-"
scrabble_name_suffix=":"
umlaut_infix="-umlaut"
with_acute_name_infix="-with-acute"
with_ogonek_name_infix="-with-ogonek"
with_overdot_name_infix="-with-overdot"
with_stroke_name_infix="-with-stroke"

def scrabblify(c):
    c_str=str(c)
    if c in string.ascii_lowercase:
        id=c_str
    elif c in polish.keys():
        c_str=polish[c]
        if c in polish_with_acute_to_base.keys():
            id=c_str + with_acute_name_infix
        elif c in polish_with_ogonek_to_base.keys(): 
            id=c_str + with_ogonek_name_infix
        elif c in polish_with_overdot_to_base.keys(): 
            id=c_str + with_overdot_name_infix
        elif c in polish_with_stroke_to_base.keys():
            id=c_str + with_stroke_name_infix
        else:
            raise ValueError(f"unknown polish character: {c}")
    elif c in german.keys():
        c_str=german[c]
        if c in umlauts.keys():
            id=c_str + umlaut_infix
        elif c in eszett.keys():
            id=c_str
        else:
            raise ValueError(f"unknown german character: {c}")
    elif c == ' ':
        id="blank" 
    else:
        raise ValueError(f"unknown polish character: {c}")
    
    return scrabble_name_prefix + id + scrabble_name_suffix


scrabblified = ''.join([scrabblify(c) for c in sys.argv[1].lower()])
print(scrabblified)

