__author__ = 'dustinlee'


import common
import shutil
import tokenize

chatFilePath = 'DATA/chat/KakaoTalkChats.txt'



def trimChatFile(fname):



    # f = open(chatFilePath, 'rb')
    # for line in f:
    #     print(repr(line))
    #     print(line)
    #
    # f.close()


    # with open(chatFilePath, 'r', encoding='utf-8-sig') as f:
    #     for line in f:
    #         print(line)
    #
    # for line in common.feedLine(chatFilePath):
    #     print(line)




    #
    with open('tmp.txt', 'wb') as f:
        f.write(b'\xef\xbb\xbf') # add utf-8 BOM
        for line in common.feedLine(chatFilePath):
            # print(repr(line))
            f.write(line.encode('utf-8'))
            f.write(b'\n')




    # with open('tmp.txt', 'wb') as f:
    #     for line in common.feedLine(fname):
    #         f.write(line.encode('utf-8'))
    #         f.write(b'\r\n')
    #
    #
    # with open('tmp.txt', 'rb') as f:
    #     for line in f:
    #         print(line.decode('utf-8'))


    shutil.copy('tmp.txt', chatFilePath)





if __name__ == "__main__":
    trimChatFile(chatFilePath)