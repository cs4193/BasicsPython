from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

    def perimeter(self):
        return 3.14*(self.radius+self.radius)

rect = Rectangle(3,5)
print(rect.area())
print(rect.perimeter())
cir = Circle(4)
print(cir.area())
print(cir.perimeter())