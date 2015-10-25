__author__ = 'dustinlee'

from common import *
import wiki
import dataset


def main():

    wiki.connect(url, 'dustinlee', 'sisa0822')

    pageID = "lecture:%4d:%02d:%s:attendance" % (year, semester, lectureName)

    headerLine = "===== %d년 %d학기 %s 출석표 =======" % (year, semester, lectureNameKorean)

#^  이름  ^  학번  ^  비고 ^


    db = dataset.connect('sqlite:///' + DBfolder + lectureDB + '.db')


    attendanceTable = db['attendance']
    keys = attendanceTable.columns[1:]
    keyLine = '^  ' + '  ^  '.join(keys) + '  ^'
    #print(keyLine)

    mainLines = []
    '''
    for row in attendanceTable:
        mainLine = '| ' + ' | '.join([row[key] for key in keys]) + '|'
        print(mainLine)
    '''

    sortedRows = attendanceTable.find(order_by=['학번'])
    print(sortedRows)

    #mainLines = '\n'.join(['| ' + ' | '.join([row[key] for key in keys]) + ' |' for row in sortedRows])


    # continuous access to row with key is a problem?
    lines = ['|  ' + '  |  '.join([row[key] for key in keys]) + '  |' for row in sortedRows]
    mainLines = '\n'.join(lines)


    pageText = '\n'.join([headerLine, keyLine, mainLines])

    print(pageText)

    print("upload to " + url + "doku.php?id=" + pageID)

    wiki.writePage(pageID, pageText)




if __name__ == "__main__":
    main()
