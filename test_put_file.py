__author__ = 'dustinlee'



import sys

from myDokuwikiXmlRpc import DokuWikiClient, DokuWikiError, DokuWikiURLError, DokuWikiXMLRPCError

import xmlrpc.client


# for remote page, put the same name of file failed
url = 'http://www.daehyunlee.com/dustinlee_new'

# for localhost, put the same named file is working, don't know why.....
url = 'http://127.0.0.1/dokuwiki'

wiki = DokuWikiClient(url, 'dustinlee', 'sisa0822')

print(wiki._dokuwiki_version())


with open('./dokuwiki.png', 'rb') as f:
    print('file live')
    #data = xmlrpc.client.Binary(f.read())
    data = f.read()

print(len(data))

try:
    wiki.delete_file(':dokuwiki.png')
except:
    pass

wiki.put_file(':dokuwiki.png', data)

