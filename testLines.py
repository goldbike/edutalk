__author__ = 'dustinlee'


prefix = "March 2, 2015, 1:11 PM, you :"

commands = """\
.lecture @0304
.lecture @0311
.lecture @0318
.lecture @0325
.report  @0325 프로그램으로 문자 보내기""".splitlines()


for line in commands:
    print(prefix + ' ' + line)


