my_list1 = [1, 2, 3]
my_list2 = [1, True, "Chetan"]
print("Initial list :", my_list1)

# Indexing
print("Indexing list :", my_list1[2])

# changing
my_list1[2] = 30
print("List after changing at index:", my_list1)

# changing multiple items in a list
my_list1[1:3] = [9, 6, 8]
print("List after changing multiple items:", my_list1)

# appending
my_list1.append(12)     # adding at the end
print("list after appending :", my_list1)

# extend
my_list1.extend([5, 6])
print("list after extend", my_list1)

# insert
my_list1.insert(2, "a")
print("list after insert", my_list1)

# remove
print(my_list1.remove(6) ) # removes the first instance of value from list it does not return anything
print("list after removing", my_list1)

# pop
print(my_list1.pop(1))    # pops the value(returns) specified by the index which was passed if no index passed last item will be poped
print("list after poping", my_list1)

# delete in list
del my_list1[1]
print("list after deleting", my_list1)

# clearing list and copy
my_list3 = my_list1.copy()
print("Copied list", my_list3)
my_list3.clear()
print("cleared list ", my_list3) # this will give [] empty list

# how to check if list is empty
if not my_list3:
    print("list is empty")
else:
    print("list is full")
my_list4 = my_list1.copy()
del my_list4
#print(my_list4) # this will give NameError as the list was deleted

# sorting
my_list1.sort()
print("sorted list ", my_list1)

# reversing
my_list1.reverse()
print("reversed list ", my_list1)

# count
print(my_list1.count(1))
