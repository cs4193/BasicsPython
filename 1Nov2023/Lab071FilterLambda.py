numbers = [10, 12, 11, 1, 2, 27]
list_numbers_greater_than_10 = list(filter(lambda x:x>10,numbers))
print(list_numbers_greater_than_10)

num_tuple = (10, 12, 11, 1, 2, 27)
tuple_numbers_greater_than_10 = tuple(filter(lambda x:x>10,num_tuple))
print(tuple_numbers_greater_than_10)