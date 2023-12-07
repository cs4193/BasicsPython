list1 = [10,1,2,3,5,8]
list1.sort()
print("the smallest number in the list", list1[0])
print("the largest number in the list", list1[len(list1)-1])

x = 0
for i in range(0,len(list1)):
    x = x + list1[i]
y = 1
for i in range(0,len(list1)):
    y = y * list1[i]

print("the sum of numbers in list",x)
print("the product of numbers in list",y)
