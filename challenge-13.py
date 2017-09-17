""""
Python Challenge Level 13.

The page title is 'call him' and there is an image of a phone with the hint
'phone that evil'. '/phonebook.php' is an XMLRPC endpoint.
"""
from xmlrpc import client

BASE_URL = 'http://www.pythonchallenge.com/pc/phonebook.php'


proxy = client.ServerProxy(BASE_URL)
# Calling 'system.listMethods()' on the proxy shows 'phone()' as the only
# non-system method. It has the help text 'Returns the phone of a person' and
# the signature [['string', 'string']].

# In challenge 12 we learnt that 'Bert is evil' so let's look him up:
print(proxy.phone('Bert'))
# '555-ITALY'
# http://www.pythonchallenge.com/pc/return/italy.html is the next URL.
