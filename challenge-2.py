"""
Python Challenge Level 2.

The hint is 'recognize the characters. maybe they are in the book, but MAYBE
they are in the page source.'. The page title is 'ocr'.

In the source code is a block comment with a large set of characters (I have
put these in the file text-ch-2.txt) and this comment:
'find rare characters in the mess below:'
"""

INPUT_FILE = 'text-ch-2.txt'

# Determine the 'rare' letters:
frequencies = {}
with open(INPUT_FILE) as f:
    for line in f:
        for c in line.strip():
            if c in frequencies:
                frequencies[c] += 1
            else:
                frequencies[c] = 1
print(''.join([c for c in frequencies if frequencies[c] == 1]))
# 'equality'
# http://www.pythonchallenge.com/pc/def/equality.html is the next URL.
