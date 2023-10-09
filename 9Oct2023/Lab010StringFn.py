name = "cHetan"  # bunch of characters immutable in nature , once created cannot be changed
#   name[0]= 'f'    throws error "TypeError: 'str' object does not support item assignment"

result = name.capitalize()
print(result)   # Chetan

result1 = name.upper()
print(result1)   # CHETAN

result2 = name.lower()
print(result2)  # chetan

result3 = name.swapcase()
print(result3)

print(id(result))   # id- Return the identity(location/address reference) of an object. Universal function
print(id(result1))
print(id(result2))

name1 = "hello world"
print(name1.title())    # Hello World
print(name1.capitalize())   # Hello world

print(len(name1))

text = "hello world"
result4 = text.replace("world","pyhon")
print(result4)  # hello python

print(text.find("world"))   # returns lowest index of the string which is being searched
print(text.find("l"))   # 2
print(text.find("L"))   # -1 as find is case-sensitive

print(text.count("l"))  # 3

name2 = "pramod"
print(name2)
del name2   # willl delete this variable from memeory
print(name2)
