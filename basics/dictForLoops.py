# print keys of a dictionary using for loop

dict1 = {80: 'http', 23: 'ftp'}
for each in dict1:
    print('Keys is dict1', each)

# printing keys & values both

for each in dict1.items():
    print(each)

# another way for printing items
print('keys\t value')
for k, v in dict1.items():
    print(k, " :\t", v)

# check for type of method returns.
dict1 = {1: 'Ajay', 2: 'Sagar'}
k = dict1.keys()
print(type(k))
v = dict1.values()
print(type(v))
i = dict1.items()
print(i)
print(type(i))
