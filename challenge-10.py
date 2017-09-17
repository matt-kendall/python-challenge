"""
Python Challenge Level 10.

The image of the bull is a link to a file 'sequence.txt' containing:
    a = [1, 11, 21, 1211, 111221,
The clue is 'len(a[30]) = ?'. This is the 'look-and-say' sequence and we
need the 30th number.
"""
import re


def next_look_say(current_value):
    """
    Given a numeric string, find it's 'look-and-say' value to determine the
    next value in the sequence.
    """
    # Split into groups of same consecutive digits
    r = '(1+|2+|3+|4+|5+|6+|7+|8+|9+|0+)'
    matches = re.findall(r, current_value)
    return ''.join([str(len(m)) + m[0] for m in matches])


a = ['1']
while len(a) <= 30:
    a.append(next_look_say(a[-1]))
print(len(a[30]))
# 5808
# http://www.pythonchallenge.com/pc/return/5808.html is the next URL.
