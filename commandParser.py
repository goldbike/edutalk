__author__ = 'dustinlee'



from pyparsing import *


# public members and functions

LECTURE, PRESENT, ABSENT, LATE, REPORT, USER, NOCOMMAND = [i for i in range(7)]




# first parseLine call includes _makeSyntax()
# succeeding call does not include _makeSyntax()
# only one time call to _makeSyntax()

def _parseLine(line):
    global syntax
    try:
        result = syntax.parseString(line)
        #print(result)
        return result
    except:
        print('parse error @' + line)


def _makeSyntaxAndParseLine(line):
    global parseLine
    _makeSyntax()
    parseLine = _parseLine
    return _parseLine(line)



parseLine = _makeSyntaxAndParseLine





# private members and functions


def _main():
    _testSyntax()



def _testSyntax():
    commands = """\
.user 이대현, 89418022
.lecture @0304
.lecture @0311
.lecture @0318
아무것도 아닌....

.absent 이대현, 김대중, 노무현
.absent @0601 박근혜, 이명박
.lecture @0325
.present @0327 이대현, 김대중, 노무현
.report  @0325 프로그램으로 문자 보내기""".splitlines()

    for line in commands:
        result = parseLine(line)
        print(result)


syntax = None

def _makeSyntax():

    global syntax

    unicodePrintables = ''.join(chr(c) for c in range(1,65536) if not chr(c).isspace() and chr(c) != ':' and chr(c) != ',')
    allChars = ''.join(chr(c) for c in range(65536))
    name = Word(unicodePrintables)
    string = Word(allChars)

    newDate = '@' + Word(nums)
    newDate.setParseAction(lambda t: int(t[1]))
    nameList = Group(delimitedList(name))
    #reportTitle = string + ZeroOrMore(" " + string)
    reportTitle = string


    absent = Keyword(".absent").setParseAction(replaceWith(ABSENT))
    late = Keyword(".late").setParseAction(replaceWith(LATE))
    present = Keyword(".present").setParseAction(replaceWith(PRESENT))
    lecture = Keyword(".lecture").setParseAction(replaceWith(LECTURE))
    report = Keyword(".report").setParseAction(replaceWith(REPORT))
    user = Keyword(".user").setParseAction(replaceWith(USER))

    absentLine = absent + Optional(newDate) + nameList

    lateLine = late + Optional(newDate) + nameList

    presentLine = present + Optional(newDate) + nameList

    lectureLine = lecture + Optional(newDate)

    reportLine = report + Optional(newDate) + reportTitle

    userLine = user + name + Suppress(Literal(",")) + name

    normalLine = string + stringEnd
    normalLine.setParseAction(lambda t: [NOCOMMAND] + [t[0]])

    blankLine = stringEnd
    blankLine.setParseAction(lambda t: [NOCOMMAND])

    syntax = blankLine | absentLine | lateLine | presentLine | lectureLine | reportLine | userLine | normalLine







if __name__ == "__main__":
    _main()

