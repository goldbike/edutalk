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


totalDate = month + date + comma + year


result = totalDate.parseString("March 25, 2015")


print(result)