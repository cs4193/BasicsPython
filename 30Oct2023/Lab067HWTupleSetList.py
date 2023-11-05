my_tuple = (15, 8, 25, 36, 42, 10)
my_tuple_list = list(my_tuple)
my_tuple_list.sort()

print("Maximum number in tuple is :",my_tuple_list[len(my_tuple_list)-1])
print("Minimum number in tuple is :",my_tuple_list[0])
print("Maximum number in tuple is :",max(my_tuple))
print("Minimum number in tuple is :",min(my_tuple))
print("************intersection and union of two sets***************")
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = set1.intersection(set2)
print("intersection of set1 and set2 ", set3)
set4 = set1.union(set2)
print("union of set1 and set2 ", set4)

print("************Remove duplicate elements from a list.***************")
my_list = [1, 2, 2, 3, 4, 4, 5]
my_list = list(set(my_list))
print("List without any duplicates ", my_list)