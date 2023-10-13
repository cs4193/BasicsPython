# Identity Operators returns Boolean used in list tuple dict set
# not to be used with other data types
# is returns true if both variables are same object
# is not returns true if both variables are not same object

x = [1, 2, 3]
y = [1, 2, 3]

print(x is y)   # False as both the variables do not have same address
print(x is not y)   # True