numbers = [1,2,3,4,5,6,7,8,9,10]
def is_even(num):
    return num %2 == 0

even_numbers = filter(is_even,numbers)
even_numbers_list = list(even_numbers)
print(even_numbers_list)

def is_positive(num):
    return num > 0


numbers1 = [1,-2,3,4,-5,6,7,-8,9,-10]
positive_num = list(filter(is_positive,numbers1))
print(positive_num)

num_map = list(map(is_positive,numbers1))
print(num_map)