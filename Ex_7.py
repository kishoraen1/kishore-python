values = ('Kishore', 'Malini', 'Lakshana', 'Tanishka')
keys = ['Father', 'Mother', 'Daughter1', 'Daughter2']

data = dict(zip(keys,values))

print(data.__len__())
print(data)
data.__delitem__('Father')

print(len(data))
print(data)
