a = int(input("Enter first number \n"))
b = int(input("Enter second number \n"))
c= a-b
result = "a is greater than b" if c > 0 else "a is less than b" if c < 0 else "a and b are equal"
print(result)