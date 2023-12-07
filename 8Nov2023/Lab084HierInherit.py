# Hierarchical Inheritance:
class Vehicle:
    def info1(self):
        return "This is a vehicle."


class Car(Vehicle):
    def info(self):
        return "This is a car."
    def info2(self):
        return "This is a car inherited"

class Benz(Car):
    def info(self):
        return "This is a Benz."

class Bicycle(Vehicle):
    def info(self):
        return "This is a bicycle."


car = Car()
bicycle = Bicycle()
print(car.info())
print(car.info1())

print(bicycle.info())
print(bicycle.info1())

benz = Benz()
print(benz.info())
print(benz.info2())
print(benz.info1())
