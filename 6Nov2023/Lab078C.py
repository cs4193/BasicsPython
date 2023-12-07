class Person:

    def __init__(self):
        print("you created an object with no arguments")

    def __init__(self, name):
        self.name = name
        print("you created an object")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("you created an object with 2 arguments")



    def printDetails(self):
        print("Your details is ",self.name)


amit = Person("amit",23)
amit.printDetails()
akshay = Person("Akshay",20)
akshay.printDetails()
