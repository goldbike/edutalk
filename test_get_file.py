__author__ = 'dustinlee'



import sys

from myDokuwikiXmlRpc import DokuWikiClient, DokuWikiError, DokuWikiURLError, DokuWikiXMLRPCError

import xmlrpc.client

url = 'http://www.daehyunlee.com/dustinlee_new'
#url = 'http://127.0.0.1/dokuwiki'

wiki = DokuWikiClient(url, 'dustinlee', 'sisa0822')

print(wiki._dokuwiki_version())


file = wiki.get_file('wiki:dokuwiki-128.png')
print(type(file.data))

with open('./dokuwiki.png', 'wb') as f:
    f.write(file.data)



