dict1 = {'a':1 , 'b':2, 'c': 3, 'd':4}
val = dict1.pop('a')
print(val)

print(dict1)
print(dir(dict1))   # this is used to get all the functions for given data type

# how to iterate a dictionary
dict2 = {'a':1 , 'b':2, 'c': 3, 'd':4}
print(len(dict2))

for k,v in dict2.items():
    print(k,v)


