dict1 = {'a':1 , 'b':2, 'c': 3, 'd':4, 'a':5}
print(dict1)    # duplicate keys
keys = dict1.keys()
values = dict1.values()
keys_list = list(keys)
values_list = list(values)
print(keys)
print(values)
print(keys_list[2])
dict2 = dict1.copy()
print(dict2)
dict2.clear()
print(dict2)
print(dict1.items())