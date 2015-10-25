__author__ = 'dustinlee'

import os


import dataset



import wiki
from common import *


def main():

    wiki.connect(url, 'dustinlee', 'sisa0822')

    pageID = "lecture:%4d:%02d:%s:attendance" % (year, semester, lectureName)
    headerLine = "===== %d년 %d학기 %s 리포트  =======" % (year, semester, lectureNameKorean)

#^  이름  ^  학번  ^  비고 ^


    db = dataset.connect('sqlite:///' + DBfolder + lectureDB + '.db')


    reportInfoTable = db['reportInfo']
    userFileTable = db['userFile']

    reportTable = db['report']
    keys = reportTable.columns[1:]
    keyLine = '^  ' + '  ^  '.join(keys) + '  ^'
    #print(keyLine)

    mainLines = []
    '''
    for row in attendanceTable:
        mainLine = '| ' + ' | '.join([row[key] for key in keys]) + '|'
        print(mainLine)
    '''

    sortedRows = reportTable.find(order_by=['학번'])
    print(sortedRows)

    userNoList = [row['학번'] for row in sortedRows]
    dateList = reportTable.columns[2:]


    mainLines = ''
    for no in userNoList:
        mainLines = mainLines + '|  ' + no
        for date in dateList:
            val = reportTable.find_one(학번=no)[date]
            if val != '미제출':
                for fname in val.split():
                    val = '{{' + pageID + ':' + fname + '?linkonly| }}'
                    print('uploading %s to %s' % (fname, pageID))
                    wiki.uploadFile(pageID, DBfolder + fname)

            mainLines = mainLines + '  |  ' + val
        mainLines = mainLines + '  |\n'


    print(mainLines)






    sortedRows = reportInfoTable.find(order_by=['date'])
    lines = ['* %s : %s' % (row['date'], row['name']) for row in sortedRows]
    infoLines = '\n'.join(lines)



    pageText = '\n'.join([headerLine, keyLine, mainLines, infoLines])

    print(pageText)

    print("upload to " + url + "doku.php?id=" + pageID)

    wiki.writePage(pageID, pageText)






if __name__ == "__main__":
    main()
