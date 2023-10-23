n = int(input("Enter the number for desired factorial \n"))
res = 1
if n < 0:
    print("Factorial of negative number is not possible")
else:
    for i in range(1, n+1):
        res = res * i

print(res)
