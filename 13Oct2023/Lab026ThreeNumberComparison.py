a = int(input("Enter first number \n"))
b = int(input("Enter second number \n"))
c = int(input("Enter third number \n"))

result = "a is the largest " if (a>b and a>c) else "b is the largest" if (b>c) else "c is the largest"
print(result)