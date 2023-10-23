year1 = int(input("enter the year \n"))

if (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0):
    res = "Leap year"
else:
    res = "not a leap year"
print(f"{year1} is {res}")
