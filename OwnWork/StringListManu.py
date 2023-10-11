str = "hello i am chetan"
list1 = list(str)   # this will convert the string into list in ordered way
print(list1)
set1 = set(str)     # this will convert the string into set which is unordered but with no duplicates
print(list1[1])
list1[2]= "Meow"
print(list1)
str2 = ''.join(list1)   # o/p heMeowlo i am chetan
print(str2)
str3 = '.'.join(list1)  #o/p h.e.Meow.l.o. .i. .a.m. .c.h.e.t.a.n
print(str3)

"""Deleting a character from a string"""
print("--------Deleting a character from a string----------")
str4 = "Hello aCHetan"
print(str4)
str5 = str4[:6] + str4[7:]
print(str5)
