__author__ = 'dustinlee'



import sys
from dokuwiki_dustin import DokuWiki, DokuWikiError




try:
    wiki = DokuWiki('http://www.daehyunlee.com/dustinlee_new/', 'dustinlee', 'sisa0822')
except DokuWikiError as err:
    print(err)
    sys.exit(1)

print(wiki.version) # => 'Release 2012-10-13 "Adora Belle"'
#print(wiki.title)
print(wiki.xmlrpc_supported_version)
print(wiki.xmlrpc_version)
print(wiki.time)
#print(wiki.login('dustinlee', 'sisa0822'))
print(wiki.pages.get('studentaccess:2015:01:gameengine:a:project'))
#print(wiki.pages.set('lecture:2016', 'new pages 0g0g0g하하하'))

wiki.medias.add(':lecture:2016:test3.png', 'testtest.png')

#print(wiki.pages.list('lecture:2014'))
#print(wiki.pages.list()) # list all pages of the wiki
#print(wiki.pages.list('my:namespace')) # list all pages in the given namespace
#print(wiki.pages.get('my:namespace:page')) # print the content of the page