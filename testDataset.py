__author__ = 'dustinlee'




import dataset

#db = dataset.connect('sqlite:///test.db')
db = dataset.connect('sqlite:///:memory:')


table = db['test']
table.insert(dict(name='이 대 현', data=89418022))

table = db['userInfo']
data = {'한글키이' : '한글 value', '또 한글 키이' : '또한글 value'}
data1 = dict(name='dustin', no='89418022')
data2 = dict(name='herbert', no='030703')


print(db.tables)
print(db['userInfo'].columns)

table.insert(data1)
table.insert(data2)


row = table.find_one(name='dustin')

print(row['no'])

print(table.find_one(name='herbert')['no'])

for r in table.find(name='dustin'):
    print(r['no'])


# getting

print(table.all())
print(table.columns[0], table.columns[1])
for e in table.all():
    print(e['no'], e['name'])



