class Customer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am ",self.name,"and I am ",self.age)

c1 = Customer("Chetan",30)
c2 = Customer("Akshatha",27)
c3 = Customer("Ankit",32)

L1 = [c1, c2, c3]
for x in L1:
    x.intro()