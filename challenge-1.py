"""
Python Challenge Level 1.

An image of a notepad with what appear to be letter transformations:
    K -> M
    O -> Q
    E -> G
And the following hint:
'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr
gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.''
"""
from string import ascii_lowercase

HINT = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc " \
       "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr " \
       "gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. " \
       "lmu ynnjw ml rfc spj."
ALPHA_SHIFT = 2  # The clue implies a caesar cipher of shift 2.


def shift_alphabet(string, shift):
    """
    Shift an input strings letters through the alphabet by a specified shift.
    """
    old_map = ascii_lowercase
    new_map = old_map[shift:] + old_map[:shift]
    return string.translate(str.maketrans(old_map, new_map))


print(shift_alphabet(HINT, ALPHA_SHIFT))
# 'i hope you didnt translate it by hand. thats what computers are for.
#  doing it in by hand is inefficient and that's why this text is so long.
#  using string.maketrans() is recommended. now apply on the url.''

# Performing the same substitution on the URL ('map'):
URL = 'map'
print(shift_alphabet(URL, ALPHA_SHIFT))
# 'ocr'
# http://www.pythonchallenge.com/pc/def/ocr.html is the next URL.
