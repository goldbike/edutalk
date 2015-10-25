__author__ = 'dustinlee'

import time
import os
import shutil

import dataset
from openpyxl import load_workbook


import katalkParser
import commandParser
import wiki
import LectureDB
import common




# input file : chat file, excel file ==> exist in some folder
# lecture info : year, semester, name, koreanName

year = 2015
semester = 2
title = '2DGameProgramming'
koreanTitle = '2D 게임 프로그래밍'
chatFilePath = 'DATA/chat/KakaoTalkChats.txt'
excelFilePath = '.\\DATA\\chat\\주1반.xlsx'


def readExcelStudentInfo(fname):
    wb = load_workbook(filename=fname)
    sheet = wb['Table2']
    for row in sheet.rows[5:]:
        # student no, name
        yield row[1].value, row[4].value


def readKatalkUserInfo(fname):
    for line in common.feedLine(fname):
        print(line)
        result = katalkParser.parseLine(line)
        if 'TALK_LINE' == result[0]:
            #print(result)
            date, year, talkTime, katalkID, talk = result[1:]
            cmd = commandParser.parseLine(talk)
            if commandParser.USER == cmd[0]:
                yield katalkID, cmd[1], cmd[2] # .user 이대현, 89418022

def main():

    LectureDB.create(year, semester, title, koreanTitle)

    # insert student info using 출석부 file ==> student no, name
    for no, name in readExcelStudentInfo(excelFilePath):
        LectureDB.insertStudent(no, name, None) # katalk ID = None, not yet assigned

    # read katalk chat, extract matching katalk ID, name, no, update student info DB
    for katalkID, name, no in readKatalkUserInfo(chatFilePath):
        if not LectureDB.studentExists(no=no):
            print('Error: invalid student no - does not exist')
        if not LectureDB.studentExists(name=name):
            print('Error: invalid student name - does not exist')
        else:
            LectureDB.updateStudent(no, name, katalkID)



    attendanceTable = db['attendance']
    reportTable = db['report']
    reportInfoTable = db['reportInfo']
    userInfoTable = db['userInfo']

    userFileTable = db['userFile'] # user upload file info
    for info in userInfoList:
        userFileTable.upsert(dict(학번=info.no), ['학번'])

    def processHostLine(date, year, talkTime, id, talk):
        cmd = commandParser.parseLine(talk)

        if commandParser.LECTURE == cmd[0]:
            if len(cmd) == 2:
                date = cmd[1] # .lecture @0304

            dateKey = '%d월 %d일' % ((date // 100), (date % 100))

            #print('making no %s table' % dateKey)
            dataList = []
            for row in userInfoTable:
                data = {'학번': row['no'], dateKey : 'O'} # default O --> attended
                dataList.append(data)

            #print(dataList)
            for data in dataList:
                attendanceTable.upsert(data, ['학번'])

            '''
            for row in attendanceTable:
                print(row)
            '''

        elif commandParser.REPORT == cmd[0]:
            if len(cmd) == 2: # .report 리포트
                reportName = cmd[1]
            elif len(cmd) == 3:
                date = cmd[1] # .report @0325 소스분석
                reportName = cmd[2]

            dateKey = '%d월 %d일' % ((date // 100), (date % 100))

            reportInfo = dict(date=dateKey, name=reportName)
            reportInfoTable.upsert(reportInfo, ['date'])


            dataList = []
            for row in userInfoTable:
                data = {'학번': row['no'], dateKey : '미제출'} # default X --> report not submitted
                dataList.append(data)

            for data in dataList:
                reportTable.upsert(data, ['학번'])

            '''
            for row in reportTable:
                print(row)
            '''

        elif commandParser.ABSENT == cmd[0]:
            if len(cmd) == 2: # .absent 이명박, 박근혜
                absentStudents = cmd[1]
            elif len(cmd) == 3:
                date = cmd[1] # .absent @0325 이명박, 박근혜
                absentStudents = cmd[2]

            dateKey = '%d월 %d일' % ((date // 100), (date % 100))






    for line in feedLine(katalkFileName):
        result = katalkParser.parseLine(line)
        if 'TALK_LINE' == result[0]:
            date, year, talkTime, id, talk = result[1:]
            fname = talk.split()[-1] # extract the last word from talk
            ext = os.path.splitext(fname)[-1]
            if len(ext) > 3: # this could file
                path = katalkFolder + fname
                if os.path.isfile(path):
                    try:
                        no = userInfoTable.find_one(katalkID=id)['no']
                        dateKey = '%d월 %d일' % ((date // 100), (date % 100))
                        data = {'학번': no, dateKey : fname}
                        shutil.copyfile(path, DBfolder + fname)
                        userFileTable.upsert(data, ['학번'])
                    except:
                        print('ERROR: ID %s is not registered.' % id)


        elif 'HOST_LINE' == result[0]:
            processHostLine(*result[1:])






    # update report db according to userInfo, userFileInfo, reportInfo


    # prepare report date list
    dateList = [row['date'] for row in reportInfoTable.all()]
    print(dateList) # now we have ['3월 25일', '4월 1일']

    userList = [row['학번'] for row in reportTable.all()]
    print(userList) # now we have ['201532', '89419022', '123456']

    for dateKey in dateList:
        for userKey in userList:
            # find upload file for the user and the date
            fname = userFileTable.find_one(학번=userKey)[dateKey]
            if fname == None:
                fname = '미제출'
            data = {'학번' : userKey, dateKey : fname}
            reportTable.upsert(data, ['학번'])



#LECTURE, PRESENT, ABSENT, LATE, REPORT, NOCOMMAND








if __name__ == "__main__":
    main()



