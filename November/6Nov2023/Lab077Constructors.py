class Car:
    name = "CHetan"     # class variable

    def __init__(self,make, model):     # default constructor
        self.make = make        # Instance variables
        self.model = model      # Instance variables
        print("i will be called first")

    def start_engine(self):
        print("starting engine "+ self.make, self.model)


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "City")
print(id(car1))
print(id(car2))
car1.start_engine()
car2.start_engine()