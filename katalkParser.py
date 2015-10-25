__author__ = 'dustinlee'


# references: http://www.ptmcg.com/geo/python/confs/TxUnconf2008Pyparsing.html



from pyparsing import *

syntax = None

def _makeSyntax():

    comma = Suppress(Literal(","))
    colon = Suppress(Literal(":"))

    months = ['January', 'February', 'March','April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    month = Word(alphas)
    month.setParseAction(lambda t: months.index(t[0]) + 1)

    date = Word(nums)
    date.setParseAction(lambda t: int(t[0]))

    year = Word(nums)
    year.setParseAction(lambda t: int(t[0]))


    talkDate = month + date + comma + year
    talkDate.setParseAction(lambda t: [t[0]*100+t[1], t[2]])

    hour = Word(nums)
    hour.setParseAction(lambda  t: int(t[0]) )

    min = Word(nums)
    min.setParseAction(lambda  t: int(t[0]) )

    ampm = (Literal("PM") | Literal("AM"))

    talkTime = hour + colon + min + ampm
    talkTime.setParseAction(lambda t: [t[0]*100+t[1]] if t[2] == 'AM' else [(t[0]+12)*100+t[1]])

    unicodePrintables = ''.join(chr(c) for c in range(65536) if not chr(c).isspace() and chr(c) != ':' and chr(c) != ',')
    string = Word(unicodePrintables)
    id = Combine(string + ZeroOrMore(" " + string))

    #talkChars = ''.join(chr(c) for c in range(65536) if not chr(c).isspace())
    #talkChars = ''.join(chr(c) for c in range(65536))
    #talkString = Word(talkChars)
    #talk = Combine(talkString + ZeroOrMore(" " + talkString))

    allChars = ''.join(chr(c) for c in range(65536))
    allString = Word(allChars)

    # KakaoTalk Chats 2015 엔컴 전공입문 (43)
    headerLine = Literal("KakaoTalk Chats") + allString
    headerLine.setParseAction(lambda t: ['HEADER'])


    # OLD: Date Saved : April 2, 2015, 12:38 PM
    # NEW: Date Saved : 9:36AM, October 10, 2015
    saveDateLine = Literal("Date Saved") + colon + talkTime + comma + talkDate
    saveDateLine.setParseAction(lambda t: ['SAVE_DATE'] + [e for e in t])

    # OLD style: March 18, 2015, 12:18 PM
    # NEW style: 12:18 PM, March 18, 2015
    dateLine = talkTime + comma + talkDate  + stringEnd
    dateLine.setParseAction(lambda t: ['DATE_LINE'] + [e for e in t])

    # March 18, 2015, 12:18 PM, 강나은 invited Mr.Lee.
    inviteLine = talkTime('time') + comma + talkDate('date') + comma + allString
    inviteLine.setParseAction(lambda t: ['INVITE_LINE'] + [e for e in t])

    hostLine = talkTime('time')  + comma + talkDate('date') + comma + Literal("you") + colon + allString
    hostLine.setParseAction(lambda t: ['HOST_LINE'] + [e for e in t])

    talkLine = talkTime('time') + comma + talkDate('date') + comma + id("ID") + colon + allString("talk")
    talkLine.setParseAction(lambda t: ['TALK_LINE'] + [e for e in t])

    blankLine = stringEnd
    blankLine.setParseAction(lambda t: ['BLANK_LINE'])

    global syntax
    syntax = headerLine | saveDateLine | hostLine | talkLine("KKK") | inviteLine | dateLine | blankLine


def _parseLine(line):
    return syntax.parseString(line.strip('\n'))


def _makeSyntaxAndParseLine(line):
    global parseLine
    _makeSyntax()
    parseLine = _parseLine
    return _parseLine(line)

parseLine = _makeSyntaxAndParseLine


if __name__ == "__main__":
    chatFileName = '.\\DATA\\userid\\KakaoTalkChats.txt'
    init()
    for result in parseFile(chatFileName):
        print(result)
        if 'HOST_LINE' == result[0]:
            print(result.host)












