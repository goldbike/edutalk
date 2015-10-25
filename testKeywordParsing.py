__author__ = 'dustinlee'



from pyparsing import *


commands = """\
.lecture @0304
.lecture @0311
.lecture @0318
.lecture @0325
.present @0327 이대현, 김대중, 노무현
.report  @0325 프로그램으로 문자 보내기
.absent  @0324 이명박, 박근혜""".splitlines()


syntax = None


def makeSyntax():

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


    def setAbsent(s,l,t):
        print(type(s), s)
        print(type(l), l)
        for e in t:
            print(e)

    absent = '.absent' + Optional(newDate) + nameList + stringEnd
    absent.setParseAction(lambda t: ['instr'] + [e for e in t])

    late = '.late' + Optional(newDate) + nameList + stringEnd
    present = '.present' + Optional(newDate) + nameList + stringEnd
    lecture = '.lecture' + Optional(newDate) + stringEnd
    report = '.report' + Optional(newDate) + reportTitle + stringEnd

    syntax = absent | late | present | lecture | report




def testSyntax():
    global syntax
    for line in commands:
        try:
            result = syntax.parseString(line)
            print(result)
        except:
            print('parse error @' + line)


def main():
    makeSyntax()
    testSyntax()



if __name__ == "__main__":
    main()

