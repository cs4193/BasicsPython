# try except
# try except else finally and nested except

# try except and nested except
try:
    num1 = int(input("Enter num1 "))
    num2 = int(input("Enter num2 "))
    result = num1/num2
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Num2 is Zero")
else:
    print(f"Result is {result}")
finally:
    print("I will always be executed")