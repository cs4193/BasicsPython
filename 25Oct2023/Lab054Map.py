double = lambda x: x**2
list1 = [1,2,3,4,5]
list2 = list(map(double,list1))
print(list2)


def quadraple(a):
    return a ** 4


list3 = list(map(quadraple,list1))
print(list3)
