__author__ = 'dustinlee'

import time
import os
import dataset
from openpyxl import load_workbook


import katalkParser
import commandParser
import common

year = 2015
semester = 2
title = '2DGameProgramming'
koreanTitle = '2D게임프로그래밍'
chatFile = 'DATA/chat/KakaoTalkChats.txt'
excelFile = '.\\DATA\\chat\\주1반.xlsx'


DBfolder = 'DATA/DB/'



db = None

def create(year=year, semester=semester, title=title, koreanTitle=koreanTitle):
    global db
    dbPath = "lecture_%4d_%02d_%s.db" % (year, semester, title)
    # for test, erase current DB
    if os.path.isfile(dbPath):
        os.remove(dbPath)

    db = dataset.connect('sqlite:///' + dbPath)
    # db = dataset.connect('sqlite:///:memory:')

    # annotate basic information
    tag = dict(author='Dae-Hyun Lee', time=time.asctime(), year=year, semester=semester, title=title, koreanTitle=koreanTitle)
    db['dbInfo'].upsert(tag, ['author'])


def insertStudent(no, name, katalkID):
    data = dict(no=no, name=name, katalkID=katalkID)
    db['studentInfo'].upsert(data, ['no'])


def updateStudent(no, name, katalkID):
    pass


def studentExists(**kwargs):
    return True



def updateStudentInfo(excelFile=excelFile, chatFile=chatFile):
    # create student info db using 출석부 file ==> student no, name
    table = db['studentInfo']
    for no, name in readExcelStudentInfo(excelFile):
        print(no, name)
        data = dict(no=no, name=name, katalkID=None)
        table.upsert(data, ['no'])

    # read katalk chat, extract mathing katalk ID, name, no, update student info DB
    for katalkID, name, no in readKatalkUserInfo(chatFile):
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



def testLectureDB():
    create()
    updateStudentInfo()


if __name__ == "__main__":
    testLectureDB()
