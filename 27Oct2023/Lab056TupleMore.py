tuple1 = tuple([1,2,3,4,5])
print(tuple1)
print(tuple1[1])
print(tuple1[2])
print(tuple1[3:])

#merging of tuple
tuple2 = (11,44,55)
tuple3 = tuple2 + tuple1
print(tuple3)

#converting tuple to list
print(list(tuple1))

q = 10
a, b = 12, 13
x, w, z = (48, 56, 70)
print(x)
print(w)
print(z)

tuple4 = (tuple1, tuple2)
print(tuple4)
print(tuple4[0])
print(tuple4[1])
print(tuple4[0][1])
print(tuple4[1][2])

# searching in tuple
car = ("ford","hector","fiat","logan")
print("ford" in car)
print("lambo" in car )