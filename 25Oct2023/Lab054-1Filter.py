def Even(a):
    if a % 2 == 0:
        return a


list1 = [1,2,3,4,5,6]
list3 = list(map(Even,list1))
print(list3)

even = lambda x:x % 2 == 0
list4 = list(filter(even,list1))
print(list4)