__author__ = 'dustinlee'

import time
import os
import shutil

import dataset


import common
import katalkParser
import commandParser
import wiki


from openpyxl import load_workbook


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


def readExcelStudentInfo(fname):
    wb = load_workbook(filename=fname)
    sheet = wb['Table2']
    for row in sheet.rows[5:]:
        # student no, name
        yield row[1].value, row[4].value




def updateStudentInfo():

    # create student info db using 출석부 file ==> student no, name
    table = db['studentInfo']
    for no, name in readExcelStudentInfo('.\\DATA\\chat\\주1반.xlsx'):
        print(no, name)
        data = dict(no=no, name=name, katalkID=None)
        table.upsert(data, ['no'])


    # read katalk chat, extract mathing katalk ID, name, no, update student info DB
    for katalkID, name, no in readKatalkUserInfo(katalkFileName):
        data = dict(no=no, name=name, katalkID=katalkID)

        if table.find_one(no=no) is None:
            print('Error: invalid student no - does not exist')
        if table.find_one(name=name) is None:
            print('Error: invalid student name - does not exist')
        else:
            table.update(data, ['no'])
            #print(katalkID, name, no)
            # check integrity of student info DB





    for data in table:
        if data['katalkID'] is None:
            print('Error: ' + data['name'] + ' .user 정보를 제대로 작성하지 않음.')


import LectureDB

db = LectureDB.create()



def main():
    katalkParser.init()
    commandParser.init()
    db = common.LectureDB()

    updateStudentInfo()



if __name__ == "__main__":
    main()