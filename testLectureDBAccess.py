__author__ = 'dustinlee'

import wiki
import dataset


from common import *


def main():

    db = dataset.connect('sqlite:///' + DBfolder + lectureDB + '.db')

    # get specific column list
    reportInfoTable = db['reportInfo']
    dateList = [row['date'] for row in reportInfoTable.all()]
    print(dateList)

    reportTable = db['report']
    userList = [row['학번'] for row in reportTable.all()]
    print(userList) # now we have ['201532', '89419022', '123456']

    userFileTable = db['userFile']
    for row in userFileTable.all():
        print(row)


    row = userFileTable.find_one(학번='2015184017')
    print(row)
    print(row['3월 25일'])




if __name__ == "__main__":
    main()
