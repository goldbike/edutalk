__author__ = 'dustinlee'




fileName = '.\\DATA\\chat\\eol.txt'
fileName = '.\\DATA\\chat\\eol.txt'
fileName = '.\\DATA\\chat\\KakaoTalkChats2015.txt'



def feedLine(fname = fileName):
    # https://docs.python.org/3/howto/unicode.html
    with open(fname, "rb") as f:
        final_line = b''
        for line in f:
            if line.endswith(b'\r\n'):
                final_line = final_line + line
                yield final_line.strip(b'\n').decode('utf-8-sig')
                #print(final_line.decode('utf-8-sig'))
                final_line = b''
            elif line.endswith(b'\n'):
                final_line = final_line + line.replace(b'\n', b' ')
            else:
                final_line = final_line + line
                yield final_line.decode('utf-8-sig')
                #print(final_line.decode('utf-8-sig'))
                final_line = b''



def main():
    for line in feedLine(fileName):
        print(line)


def main_test():

    with open(fileName, "rb") as f:
        final_line = b''
        for line in f:
            if line.endswith(b'\r\n'):
                final_line = final_line + line
                yield final_line.strip(b'\n')
                #print(final_line.decode('utf-8-sig'))
                final_line = b''
            elif line.endswith(b'\n'):
                final_line = final_line + line.replace(b'\n', b' ')
            else:
                final_line = final_line + line
                yield final_line
                #print(final_line.decode('utf-8-sig'))
                final_line = b''





def dummy():


    with open(fileName, "rb") as f:
        for line in f:
            print(line)

    with open(fileName,  encoding='utf-8-sig') as f:
        byte = f.read(1)
        print('(%x:' % ord(byte), byte, ')', end='')
        while byte != "":
            print('(%x:' % ord(byte), byte, ')', end='')
            byte = f.read(1)


    for line in f:
        l = line
        l = line.strip('\n')
        print(":".join("{:02x}".format(ord(c)) for c in l))

        #print(l)
        #print(l, end='')


if __name__ == "__main__":
    main()


