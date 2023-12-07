square = [1, 4, 9,16,25]
l = square
l2 = square.copy()
print(l)
print(l2)
print("**********************************")
square[1]= 12
print(l)
print(l2)
print("**********************************")
for x in square:
    print(x)
print("**********************************")
for y in range(len(l2)):
    print(l2[y])
print("**********************************")
[print(x) for x in l]

print("***************Reverse indexing*******************")
print(square)
print(square[-2])
print(square[-4:-2])

print("***************slicing*******************")
print(square[0:3])


