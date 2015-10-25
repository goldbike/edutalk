__author__ = 'dustinlee'


from pyparsing import *

unicodePrintables = ''.join(chr(c) for c in range(65536) if not chr(c).isspace())

string = Word(unicodePrintables)

id = Combine(string + ZeroOrMore(" " + string))

final = id

result = final.parseString("95 이대:현")

print(result)