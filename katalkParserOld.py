__author__ = 'dustinlee'


from pyparsing import *

syntax = None



lineType = None

def markHeaderLine():
    global lineType
    lineType = 'headerLine'

def markSaveDateLine():
    global lineType
    lineType = 'saveDateLine'


def markDateLine():
    global lineType
    lineType = 'dateLine'


def markInviteLine():
    global lineType
    lineType = 'inviteLine'


def markTalkLine(tokens):
    global lineType
    lineType = 'talkLine'
    if tokens[6] == 'you':
        lineType = 'professorLine'


def markBlankLine():
    global lineType
    lineType = 'blankLine'



def _makeSyntax():
    months = ['January', 'February', 'March','April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    month = Word(alphas)
    month.setParseAction(lambda t: months.index(t[0]) + 1)

    date = Word(nums)
    date.setParseAction(lambda t: int(t[0]))

    year = Word(nums)
    year.setParseAction(lambda t: int(t[0]))

    comma = Suppress(Literal(","))

    talkDate = month.setResultsName("month") + date.setResultsName("date") + comma + year.setResultsName("year")


    hour = Word(nums)
    hour.setParseAction(lambda  t: int(t[0]) )

    min = Word(nums)
    min.setParseAction(lambda  t: int(t[0]) )

    ampm = (Literal("PM") | Literal("AM"))

    talkTime = hour.setResultsName("hour") + Suppress(Literal(":")) + min.setResultsName("min") + ampm.setResultsName("ampm")

    unicodePrintables = ''.join(chr(c) for c in range(65536) if not chr(c).isspace() and chr(c) != ':' and chr(c) != ',')
    string = Word(unicodePrintables)
    id = Combine(string + ZeroOrMore(" " + string))

    talkChars = ''.join(chr(c) for c in range(65536) if not chr(c).isspace())
    #talkChars = ''.join(chr(c) for c in range(65536))
    talkString = Word(talkChars)
    talk = Combine(talkString + ZeroOrMore(" " + talkString))

    keyword = Word(alphas)
    newDate = '@' + Word(nums)



    absent = '.absent' + Optional(newDate) + nameList
    late = '.late' + Optional(newDate) + nameList
    present = '.present' + Optional(newDate) + nameList
    lecture = '.lecture' + Optional(newDate)
    report = '.report' + Optional(newDate) + reportTitle








    # KakaoTalk Chats 2015 엔컴 전공입문 (43)
    headerLine = Literal("KakaoTalk Chats") + Combine(string + ZeroOrMore(" " + string)) + stringEnd
    headerLine.setParseAction(markHeaderLine)


    # Date Saved : April 2, 2015, 12:38 PM
    saveDateLine = Literal("Date Saved") + ":" + talkDate('saveDate') + "," + talkTime('saveTime') + stringEnd
    saveDateLine.setParseAction(markSaveDateLine)

    # March 18, 2015, 12:18 PM
    dateLine = talkDate + "," + talkTime + stringEnd
    dateLine.setParseAction(markDateLine)

    # March 18, 2015, 12:18 PM, 강나은 invited Mr.Lee.
    inviteLine = talkDate('date') + "," + talkTime('time') + "," + Combine(string + ZeroOrMore(" " + string)) + stringEnd
    inviteLine.setParseAction(markInviteLine)


    talkLine = talkDate('date') + Suppress(Literal(",")) + talkTime('time') + Suppress(Literal(",")) + id("ID") + Suppress(Literal(":")) + talk("talk") + stringEnd
    talkLine.setParseAction(markTalkLine)

    global syntax
    syntax = stringEnd.setParseAction(markBlankLine) | headerLine | saveDateLine | dateLine | inviteLine | talkLine


def parseFile(fname):
    _makeSyntax()
    # https://docs.python.org/3/howto/unicode.html
    with open(fname, encoding='utf-8-sig') as f:
        for line in f:
            yield syntax.parseString(line.strip('\n')), lineType


def init():
    _makeSyntax()

def parseLine(line):
    return syntax.parseString(line.strip('\n')), lineType



class UserInfo(object):
    pass


def extractUserInfo(fname):
    userInfoList = []
    for result, lineType in parse(fname):
        if 'talkLine' == lineType:
            talk = result.talk.split()
            userInfo = UserInfo()
            userInfo.id = result.ID
            if len(talk) == 4: # 이름 이대현 학번 89418022 ==> 4 words
                if talk[0] == '이름' and talk[2] == '학번':
                    userInfo.name = talk[1]
                    userInfo.no = talk[3]
                    userInfoList.append(userInfo)

    return userInfoList





if __name__ == "__main__":
    chatFileName = '.\\DATA\\userid\\KakaoTalkChats.txt'
    for result, lineType in parse(chatFileName):
        print(result, lineType)









