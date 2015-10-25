__author__ = 'dustinlee'


from pyparsing import *

unicodePrintables = ''.join(chr(c) for c in range(65536) if not chr(c).isspace())

id = Word(unicodePrintables)

final = id

result = final.parseString("이대현")

print(result)