__author__ = 'dustinlee'


from pyparsing import *



date = Word(nums)
#date.setResultsName("value")
#date.setParseAction(lambda  t: int(t[0]))

final_result = date.setResultsName("value")


result = final_result.parseString("123")

print("value: ", result.value)
print("type", type(result.value))
print(result)

