def change(L):
    print(id(L))
    L.append(5)
    print(L)
    print(id(L))


L1 = [1,2,3,4]
print("original list",L1)
print(id(L1))
change(L1)
print("Changed list",L1)

print("****************now we do the same above without affecting original list")
L2 = [4,5,6,7]
print("original list",L2)
print(id(L2))
change(L2[:])
print("After Changed list original list",L2)