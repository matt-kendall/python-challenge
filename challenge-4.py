"""
Python Challenge Level 4.

The page title is 'follow the chain' and the image is a link with href
"linkedlist.php?nothing=12345". Following that URL is a page saying 'and the
next nothing is 44827', so we need to follow the chain.

There is a block comment in the page source: ' urllib may help. DON'T TRY ALL
NOTHINGS, since it will never end. 400 times is more than enough.
 """
import urllib.request
import re

STARTING_NOTHING = 12345


def make_url(nothing):
    """
    Get the URL of a given 'nothing'.
    """
    return 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d' \
            % nothing


def follow(nothing):
    """
    Follow a chain of 'nothings' to find the non-nothing at the end of the
    chain. Returns the non-nothing after calling itself recursively.
    """
    url = make_url(nothing)
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        next_nothing = find_next_nothing(body, nothing)
        if next_nothing:
            return follow(next_nothing)
        else:
            # No more to follow, completed!
            return body


def find_next_nothing(body, current_nothing):
    """
    Find the next nothing from the response body.
    """
    m = re.search('and the next nothing is ([0-9]+)', body)
    if m is not None:
        return int(m.group(1))
    else:
        if body == 'Yes. Divide by two and keep going.':
            # There is an exception to the rule where we are told to divide!
            return current_nothing / 2


print(follow(STARTING_NOTHING))
# 'peak.html'
# http://www.pythonchallenge.com/pc/def/peak.html is the next URL.
