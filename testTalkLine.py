__author__ = 'dustinlee'


from pyparsing import *


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


unicodePrintables = ''.join(chr(c) for c in range(65536) if not chr(c).isspace() and chr(c) != ':')
string = Word(unicodePrintables)
id = Combine(string + ZeroOrMore(" " + string))

talkChars = ''.join(chr(c) for c in range(65536) if not chr(c).isspace())
#talkChars = ''.join(chr(c) for c in range(65536))
talkString = Word(talkChars)
talk = Combine(talkString + ZeroOrMore(" " + talkString))


# KakaoTalk Chats 2015 엔컴 전공입문 (43)
headerLine = Literal("KakaoTalk Chats") + Combine(string + ZeroOrMore(" " + string)) + stringEnd



# Date Saved : April 2, 2015, 12:38 PM
saveDateLine = Literal("Date Saved") + ":" + talkDate.setResultsName('saveDate') + "," + talkTime.setResultsName('saveTime') + stringEnd



# March 18, 2015, 12:18 PM
dateLine = talkDate + "," + talkTime + stringEnd



# March 18, 2015, 12:18 PM, 강나은 invited Mr.Lee.
inviteLine = talkDate.setResultsName('date') + "," + talkTime.setResultsName('time') + "," + Combine(string + ZeroOrMore(" " + string)) + stringEnd



userInfo = {}


def processTalkLine(tokens):

    #print(tokens[-1])
    words = tokens[-1].split()

    #print(words)
    if len(words) == 4:
        if words[0] == '이름' and words[2] == '학번':
            name = words[1]
            userNumber = words[3]
            userInfo[name] = userNumber




talkLine = talkDate.setResultsName('date') + Suppress(Literal(",")) + talkTime.setResultsName('time') + Suppress(Literal(",")) + id.setResultsName("ID") + Suppress(Literal(":")) + talk.setResultsName("talk") + stringEnd
talkLine.setParseAction(processTalkLine)



final = stringEnd | headerLine | saveDateLine | dateLine | inviteLine | talkLine






#result = final.parseString("March 18, 2015, 1:12 PM, you : 혹시.. 안가거나 못가는 이유가 어떤 것이 있는지? ")
#result = final.parseString("KakaoTalk Chats 2015 엔컴 전공입문 (43)")
#result = final.parseString("Date Saved : April 2, 2015, 12:38 PM")
#result = final.parseString(" ")


fileName = '.\\DATA\\userid\\KakaoTalkChats.txt'


def feedLine(fname = fileName):
    # https://docs.python.org/3/howto/unicode.html
    with open(fname, encoding='utf-8-sig') as f:
        for line in f:
            yield line.strip('\n')


for line in feedLine():
    #print(line)
    result = final.parseString(line)

print(userInfo)





'''
print('DATE: %02d %02d %4d' % (result.month, result.date, result.year))

if result.ampm == "PM":
    result.hour = result.hour + 12

print('TIME: %02d:%02d' % (result.hour, result.min))


print('ID  : %s' % result.ID)
print('TALK: %s' % result.talk)

'''













