num = int(input("Enter your number \n"))
sum = 0

while num != 0:
    digit = num % 10
    sum += digit
    num //= 10
print(sum)
