__author__ = 'dustinlee'

import time
import os
import dataset

url = 'http://www.daehyunlee.com/dustinlee_new/'
url = 'http://127.0.0.1/dokuwiki/'

#katalkFileName = '.\\DATA\\userid\\KakaoTalkChats.txt'
katalkFileName = 'DATA/chat/KakaoTalkChats.txt'
katalkFolder = 'DATA/chat/'
excelName = '.\\DATA\\chat\\주1반.xlsx'


year = 2015
semester = 2
lectureName = '2DGameProgramming'
lectureNameKorean = '2D게임프로그래밍'

lectureDB = "lecture_%4d_%02d_%s" % (year, semester, lectureName)
DBfolder = 'DATA/DB/'


prefix = "March 2, 2015, 1:11 PM, you :"

#LECTURE, PRESENT, ABSENT, LATE, REPORT, NOCOMMAND

commands = """\
.user 이대현, 89418022
.present @0304 이대현, 이명박, 이건희
.absent  @0304 노무현, 김대중
.late    @0304 김영삼
.lecture @0304
.lecture @0311
.lecture @0318
.lecture @0325
.report  @0325 프로그램으로 문자 보내기""".splitlines()












def feedLine(fname):
    # https://docs.python.org/3/howto/unicode.html
    with open(fname, "rb") as f:
        final_line = b''
        for line in f:
            if line.endswith(b'\r\n'):
                final_line = final_line + line
                # strip b'\n' if exists
                yield final_line.strip(b'\n').decode('utf-8-sig')
                #print(final_line.decode('utf-8-sig'))
                final_line = b''
            elif line.endswith(b'\n'):
                final_line = final_line + line.replace(b'\n', b' ')
            else:
                final_line = final_line + line
                yield final_line.decode('utf-8-sig')
                #print(final_line.decode('utf-8-sig'))
                final_line = b''




def testFeedLine():
    for line in feedLine(katalkFileName):
        print(line)
    pass

def test1():
    with open(katalkFileName, 'rb') as f:
        for line in f:
            print(line)



def main():
    test1()


if __name__ == "__main__":
    main()