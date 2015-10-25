__author__ = 'dustinlee'

import time
import os

import dataset


import katalkParser
import commandParser
import shutil


#katalkFileName = '.\\DATA\\userid\\KakaoTalkChats.txt'
katalkFileName = 'DATA/userid/KakaoTalkChats.txt'
katalkFolder = 'DATA/userid/'

year = 2015
semester = 1
lectureName = 'gameengineeringintroduction'
lectureNameKorean = '전공입문'

lectureDB = "lecture_%4d_%02d_%s" % (year, semester, lectureName)
DBfolder = 'DATA/DB/'


prefix = "March 2, 2015, 1:11 PM, you :"

commands = """\
.lecture @0304
.lecture @0311
.lecture @0318
.lecture @0325
.report  @0325 프로그램으로 문자 보내기""".splitlines()




def feedLine(fname):

    '''
    for line in commands:
        yield (prefix + ' ' + line).strip('\n')
    '''



    with open(fname, encoding='utf-8-sig') as f:
        for line in f:
            yield line.strip('\n')



def main():

    katalkParser.init()
    commandParser.init()

    for line in feedLine(katalkFileName):
        result = katalkParser.parseLine(line)
        if 'TALK_LINE' == result[0]:
            date, year, talkTime, id, talk = result[1:]
            fname = talk.split()[-1] # extract the last word from talk
            ext = os.path.splitext(fname)[-1]
            if len(ext) > 3: # this could file
                path = katalkFolder + fname
                if os.path.isfile(path):
                    dateKey = '%d월 %d일' % ((date // 100), (date % 100))
                    data = {'학번': '894180822', dateKey : fname}
                    shutil.copyfile(path, DBfolder + fname)




if __name__ == "__main__":
    main()



