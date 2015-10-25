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


def insertStudentInfo(no, name, katalkID):
    data = dict(no=no, name=name, katalkID=katalkID)
    db['studentInfo'].upsert(data, ['no'])


def updateStudentInfo(no, name, katalkID):
    data = dict(no=no, name=name, katalkID=katalkID)
    db['studentInfo'].upsert(data, ['no'])
    pass


def findStudentInfo(**kwargs):
    # print(kwargs)
    info = db['studentInfo'].find_one(**kwargs)
    return info





def testLectureDB():
    create()
    # updateStudentInfo()


if __name__ == "__main__":
    testLectureDB()
