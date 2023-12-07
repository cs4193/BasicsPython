# Ordered Dictionary
# key values are available based on insertion(will store the k:v based on which comes first)
# list set tuple dict Ordered Dict used in API and Selenium
# use case Ordered Dict : used to store webElements in sequence in Selenium to keep order like login,dashborad elments
# dict will not keep the order of insertion
# OD keeps the order of insertion

from collections import OrderedDict

od = OrderedDict()
od['a']= 98
od['b']= 2
od['c']= 9
od['d']= 38
print(od)

dict1 = { 'b':2, 'c': 3, 'd':4, 'a':1 }
print(dict1)

# to print sortted list of keys
keys = list(dict1.keys())
print(keys)
keys_sort = sorted(keys)
keys_sort_rev = list(reversed(keys_sort))
keys_sort_rev2 = sorted(keys, reverse=True)
print("keys:",keys_sort)
print("keys reversed using reverse ",keys_sort_rev)
print("keys reversed using sort ",keys_sort_rev2)

od2 = OrderedDict()
od2[keys_sort[0]]   = 23
od2[keys_sort[1]]   = 255
od2[keys_sort[2]]   = 1
od2[keys_sort[3]]   = 2
print(od2)