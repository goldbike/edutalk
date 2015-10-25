__author__ = 'dustinlee'



import sys

from dokuwiki.dokuwikixmlrpc import DokuWikiClient, DokuWikiError, DokuWikiURLError, DokuWikiXMLRPCError

import xmlrpc.client

url = 'http://www.daehyunlee.com/dustinlee_new'
#url = 'http://127.0.0.1/dokuwiki'

wiki = DokuWikiClient(url, 'dustinlee', 'sisa0822')

print(wiki._dokuwiki_version())




wiki.put_page('lecture:2016', '잘 되나 진째??')
print(wiki.list_files(':', True))


with open('./test.jpeg', 'rb') as f:
    print('file live')
    #data = xmlrpc.client.Binary(f.read())
    data = f.read()

print(len(data))

wiki.put_file(':test2.jpeg', data)

print(type(data))


file = wiki.get_file(':test2.jpeg')
print(type(file.data))


#print(len(read_file))
#print(len(read_file))

with open('./from4.jpeg', 'wb') as f:
    f.write(file.data)




#
#
#  https://forum.dokuwiki.org/thread/7525
# not working
#
# https://github.com/gturri/dokujclient
#








#
# print(wiki.version) # => 'Release 2012-10-13 "Adora Belle"'
#print(wiki.title)
#print(wiki.xmlrpc_supported_version)
#print(wiki.xmlrpc_version)
#print(wiki.time)
#print(wiki.login('dustinlee', 'sisa0822'))
#print(wiki.pages.get('studentaccess:2015:01:gameengine:a:project'))
#print(wiki.pages.set('lecture:2016', 'new pages 0g0g0g하하하'))

#wiki.medias.add(':lecture:2016:test3.png', 'testtest.png')

#print(wiki.pages.list('lecture:2014'))
#print(wiki.pages.list()) # list all pages of the wiki
#print(wiki.pages.list('my:namespace')) # list all pages in the given namespace
#print(wiki.pages.get('my:namespace:page')) # print the content of the page