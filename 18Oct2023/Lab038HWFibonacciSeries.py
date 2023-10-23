n = int(input("Enter the length of fibonacci series \n"))
a0 = 0
a1 = 1
print(a0, end="\t")
print(a1, end="\t")
for i in range(2, n):
    a2 = a0 + a1
    print(a2, end="\t")
    a0 = a1
    a1 = a2
