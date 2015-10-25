__author__ = 'dustinlee'


# http://eli.thegreenplace.net/2010/12/14/problem-passing-arguments-to-python-scripts-on-windows/





# game engine programming uploader


import sys
import os


import wiki


url = 'http://www.daehyunlee.com/dustinlee_new/'
url = 'http://127.0.0.1/dokuwiki/'

year = 2015
semester = 1
lectureName = 'gameengine'
lectureNameKorean = '게임엔진프로그래밍'




def test():
    fname = 'herbert.jpg'
    print(len(sys.argv))
    if len(sys.argv) >= 2:
        fname = sys.argv[1]

    print(sys.argv[1:])

    im = Image.open(fname)

    im.show()

def test2():
    print(sys.version)
    print(len(sys.argv))
    if len(sys.argv) >= 2:
        print(sys.argv[1:])

    input("Press Enter to Continue...")




uploadFiles = ['d:\\Work\\Lecture\\2015 01\\Game Engine\\Labs\\distribution\\Lecture16.zip']
uploadFiles.append('d:\\Work\\Lecture\\2015 01\\Game Engine\\Slides\\PDF\\제07강 - 애니메이션.pdf')



def main():
    wiki.connect(url, 'dustinlee', 'sisa0822')

    slidesPage = "lecture:%4d:%02d:%s:slides" % (year, semester, lectureName)
    todayPage = "todayslecture:%4d:%02d" % (year, semester)

    page = wiki.readPage(slidesPage)
    lines = page.splitlines()

    for path in uploadFiles:
        fname = os.path.basename(path)
        print('uploading %s to %s' % (fname, slidesPage))
        wiki.uploadFile(slidesPage, path)


    print(lines)





















if __name__ == "__main__":
    main()


















