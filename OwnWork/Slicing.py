str = "this string will be sliced"

print(str[:8])  # this will print all characters before i as upper index is excluded
print(str[8:])  # this will print all characters after r as lower index is inclusive
print(str[:])   # prints whole string
print(str[0:-1])    # will print all characters except the last one
print(str[0:-3])    # will print all characters except the last three
print(str[::-1])    # this will reverse the string

print("-----------Slicing with a step----------------")
print(str[0:8:1])
print(str[0:8:2])
print(str[0:8:3])

print("-----------Reverse Slicing with a step----------------")
print(str[26:0:-1])
print(str[26:0:-2])
print(str[26:0:-3])
""" --------------o/p-----------------------------------
this str
ing will be sliced
this string will be sliced
this string will be slice
this string will be sli
decils eb lliw gnirts siht
-----------Slicing with a step----------------
this str
ti t
tst
-----------Reverse Slicing with a step----------------
decils eb lliw gnirts sih
dcl bli nrssh
di  igr h
---------------------------------------------------------"""
