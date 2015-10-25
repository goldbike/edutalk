__author__ = 'dustinlee'

import os


from myDokuwikiXmlRpc import DokuWikiClient, DokuWikiError, DokuWikiURLError, DokuWikiXMLRPCError

home = None

def connect(url, id, passwd):
    global home
    home = DokuWikiClient(url, id, passwd)

def writePage(id, contents):
    home.put_page(id, contents)


def readPage(id):
    return home.page(id)



#
# NOTE: maximum upload size should be adjusted at the wiki site
#
# https://www.dokuwiki.org/faq:uploadsize
#
# upload_max_filesize = 256M
# post_max_size = 256M
# memory_limit = 256M
#


def uploadFile(page, path):

    fname = os.path.basename(path)

    fileID = page + ':' + fname
    fileID = fileID.replace(' ', '_') # wiki ID shoud not have space

    print(fileID)

    with open(path, 'rb') as f:
        data = f.read()
    try:
        home.delete_file(fileID)
    except:
        pass

    home.put_file(fileID, data)


def downloadFile(id, fname):
    file = home.get_file(id)
    with open(fname, 'wb') as f:
        f.write(file.data)











