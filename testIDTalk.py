__author__ = 'dustinlee'


from pyparsing import *

unicodePrintables = ''.join(chr(c) for c in range(65536) if not chr(c).isspace() and chr(c) != ':')

string = Word(unicodePrintables)

id = Combine(string + ZeroOrMore(" " + string))

talk = Combine(string + ZeroOrMore(" " + string))

final = id + ":" + talk

result = final.parseString("95 황규진 : 이것은 테스트입니다... ㅋㅋㅋ")

print(result)