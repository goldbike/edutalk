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
# chatFilePath = 'DATA/chat/KakaoTalkChats2015.txt'
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
        # print(line)
        result = katalkParser.parseLine(line)
        if 'TALK_LINE' == result[0]:
            #print(result)
            date, year, talkTime, katalkID, talk = result[1:]
            cmd = commandParser.parseLine(talk)
            if commandParser.USER == cmd[0]:
                yield katalkID, cmd[1], cmd[2] # .user 이대현, 89418022



#LECTURE, PRESENT, ABSENT, LATE, REPORT, NOCOMMAND
def buildStudentDB():

    studentNoList = []
    # insert student info using 출석부 file ==> student no, name
    for no, name in readExcelStudentInfo(excelFilePath):
        LectureDB.insertStudentInfo(no, name, None) # katalk ID = None, not yet assigned
        studentNoList.append(no)

    # read katalk chat, extract matching katalk ID, name, no, update student info DB
    for katalkID, name, no in readKatalkUserInfo(chatFilePath):
        if LectureDB.findStudentInfo(no=no) is None:
            print('Error:', katalkID + '의 .user 정보작성에 오류가 있음. - 출석부에 학번', no, ' 존재하지 않음.')
            continue
        if LectureDB.findStudentInfo(name=name) is None:
            print('Error:', katalkID + '의 .user 정보작성에 오류가 있음. - 출석부에 이름', name, ' 존재하지 않음.')
            continue
        LectureDB.updateStudentInfo(no, name, katalkID)
        # print(no, name, katalkID)


    # check integrity of student info DB
    for no in studentNoList:
        info = LectureDB.findStudentInfo(no=no)
        # print(info)
        if info['katalkID'] is None:
            print('Error: ' , info['name']+'의 .user 정보작성에 오류가 있음.')



def testUpdateStudentInfo():
    LectureDB.create(year, semester, title, koreanTitle)
    buildStudentDB()



if __name__ == "__main__":
    testUpdateStudentInfo()

