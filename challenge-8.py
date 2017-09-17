"""
Python Challenge Level 8.

The image is a bee, with a link on a map outline of the bee. The link goes to
'good.html' but requires a username and password. In the page source is
this comment:
<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->
'BZh' is the file signature for the Bzip2 compressed file (hence 'bee'!).
"""
import bz2

USERNAME_COMPRESSED = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
PASSWORD_COMPRESSED = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print(bz2.decompress(USERNAME_COMPRESSED))
# 'huge'
print(bz2.decompress(PASSWORD_COMPRESSED))
# 'file'
# http://www.pythonchallenge.com/pc/return/good.html is the next URL
# with the authorisation provided above.
