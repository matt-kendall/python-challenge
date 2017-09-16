"""
Python Challenge Level 5.

The page title is 'peak hell' and the hint is 'pronounce it'. There is an
element in the page source:
    <peakhell src="banner.p">
        <!-- peak hell sounds familiar ? -->
    </peakhell>
The contents of http://www.pythonchallenge.com/pc/def/banner.p are in the file
'banner.p'.
"""
import pickle  # 'Peak hell' sounds like pickle

FILENAME = 'resources/banner.p'

with open(FILENAME, 'rb') as f:
    # 'peak hell' sounds like pickle:
    unpickled_list = pickle.load(f)

# It's a list of lists of 2-tuples of (ASCII character, number)
for line in unpickled_list:
    s = ''
    for pair in line:
        s += pair[0] * int(pair[1])
    print(s)
# Prints 'channel' in ASCII art.
# http://www.pythonchallenge.com/pc/def/channel.html is the next URL.
