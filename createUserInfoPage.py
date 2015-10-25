__author__ = 'dustinlee'

import katalkParser
import wiki



chatFileName = '.\\DATA\\userid\\KakaoTalkChats.txt'




def main():

    url = 'http://www.daehyunlee.com/dustinlee_new/'
    #url = 'http://127.0.0.1/dokuwiki/'

    wiki.open(url, 'dustinlee', 'sisa0822')
    year = 2015
    semester = 1
    lectureName = 'gameengineeringintroduction'
    lectureNameKorean = '전공입문'

    pageID = "lecture:%4d:%02d:%s:attendance" % (year, semester, lectureName)

    header = """\
===== %d년 %d학기 %s 출석표 =======

^  이름  ^  학번  ^  비고 ^""" % (year, semester, lectureNameKorean)


    userInfo = extractUserInfo(chatFileName)


    main = '\n'.join(['| %s | %s |' % (studentNo, userInfo[studentNo]) for studentNo in sorted(userInfo.keys())])


    pageText = header + '\n' + main


    print("upload to " + url + "doku.php?id=" + pageID)

    wiki.writePage(pageID, pageText)




if __name__ == "__main__":
    main()
