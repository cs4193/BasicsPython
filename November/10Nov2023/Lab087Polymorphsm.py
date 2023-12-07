class Shape:
    def area(self):
        print("Area of shape")


class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Ciracle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2


shape1 = Rectangle(3,4)
print(shape1.area())

shape2 = Ciracle(10)
print(shape2.area())

shape3 = Shape()
shape3.area()