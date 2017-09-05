"""
Python Challenge Level 3.

The hint is 'One small letter, surrounded by EXACTLY three big bodyguards on
each of its sides.'. The image is of three big candles surrounding a
smaller candles. In the page source is another large block comment, the contents
of which are contained in 'text-ch-3.txt'. The page title is 're' - a hint to
use regex?
"""
import re

INPUT_FILE = 'text-ch-3.txt'
# Look for exactly three uppercase letters surrounding a lowercase letter
PATTERN = '[a-z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]+'

answer = ''
with open(INPUT_FILE) as f:
    for line in f:
        m = re.search(PATTERN, line)
        if m is not None:
            answer += m.group(1)
print(answer)
# 'linkedlist'
# http://www.pythonchallenge.com/pc/def/linkedlist.html shows a page containing
# only the words 'linkedlist.php',
# http://www.pythonchallenge.com/pc/def/linkedlist.php is the next URL
