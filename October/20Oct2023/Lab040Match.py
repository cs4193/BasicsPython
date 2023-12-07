number = int(input("Enter number\n"))
match number:
    case 1:
        print("u have entereed 1")
    case 2:
        print("u have entered 2")
    case _:
        print("u have entered invalid number")

name = input("enter our name \n")
match name:
    case "Chetan":
        print("Hello Chetan")
    case "lucky":
        print("hello lucky")
    case _:
        print("hello")