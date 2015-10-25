__author__ = 'dustinlee'


from pyparsing import *

hour = Word(nums)
hour.setParseAction(lambda  t: int(t[0]) )

min = Word(nums)
min.setParseAction(lambda  t: int(t[0]) )

ampm = (Literal("PM") | Literal("AM"))

time_expr = hour.setResultsName("hour") + ":" + min.setResultsName("min") + ampm.setResultsName("ampm")

result = time_expr.parseString("12:13 PM")

print(result)

print(result.hour, result.min, result.ampm)




