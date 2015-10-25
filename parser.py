__author__ = 'dustinlee'


from pyparsing import *

'''
month = Word(alphas)
date = Word(nums)
year = Word(nums)
'''

months = ['January', 'February', 'March','April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']




hour = Word(nums)
hour.Name = 'hour'
#hour.ParseAction = lambda t: int(t[0])

#hour.setResultsName("hour")
#hour.setResultsName('hour')
hour.setParseAction(lambda  t: int(t[0]) )

min = Word(nums)
min.Name = 'min'
min.setParseAction(lambda  t: int(t[0]) )



ampm = (Literal("PM") | Literal("AM"))

time_expr = hour + ":" + min + ampm



result = time_expr.parseString("12:13 PM")

print(result[0])
a,b,c,d = result

print(a,b,c,d)

#print(result.hour, result.min, result.ampm)

print(result)

print(result.hour)

print(result.keys())
print(result.items())
print(result.values())




