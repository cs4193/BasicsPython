def sum1(num1):
    res = 0
    for num in num1:
        res = res + int(num)
    return res


num1 = input("Enter the number\n")
print(sum1(num1))
