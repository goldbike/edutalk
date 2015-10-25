__author__ = 'dustinlee'

init = False

def act2(n):
    print('act2 %d' % n)


def act1(n):
    global process
    global init
    if init is False:
        init = True
        process = act2
    print('act1 %d' % n)


process = act1
print('imported test')

for i in range(10):
    process(i+10)


