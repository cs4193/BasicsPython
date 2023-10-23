n = int(input("Enter the length of fibonacci series \n"))
a0 = 0
a1 = 1
while a0 < n:
    print(a0, end="\t")
    a0, a1 = a1, a0+a1
