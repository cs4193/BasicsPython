# string functions
my_string = "This is Chetan from testing Academy"
print(type(my_string))
print(len(my_string))

"""how to prove sstring immutable """
my_string = "This is Chetan from testing Academy"
#my_string[0]   = "h"    #TypeError: 'str' object does not support item assignment
print(my_string)

str1 = "chetan"
print(id(str1))
str1 = "shetty"
print(id(str1))
