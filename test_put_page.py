__author__ = 'dustinlee'



import sys

from myDokuwikiXmlRpc import DokuWikiClient, DokuWikiError, DokuWikiURLError, DokuWikiXMLRPCError

import xmlrpc.client

#url = 'http://www.daehyunlee.com/dustinlee_new'
url = 'http://127.0.0.1/dokuwiki'

wiki = DokuWikiClient(url, 'dustinlee', 'sisa0822')

print(wiki._dokuwiki_version())


import datetime

newText = str(datetime.datetime.now()) + '에 작성되었습니다.'
print(newText)

wiki.put_page('start', newText)
print(wiki.list_files(':', True))
    print(result.talkLine.ttalk)
