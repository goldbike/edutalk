__author__ = 'dustinlee'




def getLine():
    for i in range(10):
        yield '| %d | %d | %d | %d |' % (i,i,i,i)



a = 'first line'
b = 'second line'
c = 'third line'

lines = [a,b,c]

final = '\n'.join(getLine())

print(final)
