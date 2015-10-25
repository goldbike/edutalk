__author__ = 'dustinlee'


import sys


from PIL import Image

fname = 'herbert.jpg'
print(len(sys.argv))
if len(sys.argv) >= 2:
    fname = sys.argv[1]

print(sys.argv[1:])

im = Image.open(fname)

im.show()

