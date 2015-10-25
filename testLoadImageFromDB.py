__author__ = 'dustinlee'




import dataset

db = dataset.connect('sqlite:///test.db')


table = db['image']




e = table.find_one(name='dokuwiki.png')


import io

data = io.BytesIO(e['data'])

from PIL import Image



im = Image.frombytes()
im.show()

data.close()




#element = table.find(name='dokuwiki.png')

#print(element)


