dict1 = {'a':1 , 'b':2, 'c': 3, 'd':4}
val = dict1.pop('a')
print(val)

val = dict1.popitem() # popitem removes arbitrary key value pair
print(val)
print(dict1)

dic2 = dict1.copy()
del dic2
#print(dic2) # this will give error
dict1['a'] = 3
print(dict1)