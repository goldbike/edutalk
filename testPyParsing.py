from pyparsing import Word, Group, Combine, Suppress, OneOrMore, alphas, nums, \
    alphanums, stringEnd, ParseException
import time

num = Word(nums)
date = Combine(num + "/" + num + "/" + num)


def validateDateString(tokens):
    try:
        time.strptime(tokens[0], "%m/%d/%Y")
    except ValueError:
     raise ParseException("Invalid date string (%s)" % tokens[0])

date.setParseAction(validateDateString)
schoolName = OneOrMore(Word(alphas))
schoolName.setParseAction(lambda tokens: " ".join(tokens))
score = Word(nums).setParseAction(lambda tokens: int(tokens[0]))
schoolAndScore = Group(schoolName.setResultsName("school") + \
                       score.setResultsName("score"))
gameResult = date.setResultsName("date") + schoolAndScore.setResultsName("team1") + \
             schoolAndScore.setResultsName("team2")
tests = """\
09/04/2004 Virginia 44 Temple 14
09/04/2004 LSU 22 Oregon State 21
09/09/2004 Troy State 24 Missouri 14
01/02/2003 Florida State 103 University of Miami 2""".splitlines()
for test in tests:
    stats = gameResult.parseString(test)
    if stats.team1.score != stats.team2.score:
        if stats.team1.score > stats.team2.score:
            result = "won by " + stats.team1.school
        else:
            result = "won by " + stats.team2.school
    else:
        result = "tied"
    print("%s %s(%d) %s(%d), %s" % (stats.date, stats.team1.school, stats.team1.score,                           stats.team2.school, stats.team2.score, result))

# or print one of these alternative formats
# print "%(date)s %(team1)s %(team2)s" % stats
# print stats.asXML("GAME")