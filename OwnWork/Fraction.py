class Fraction:

    def __init__(self,num,den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        temp_num = self.num * other.den + self.den * other.num
        temp_den = self.den * other.den
        return f"{temp_num}/{temp_den}"

    def __sub__(self, other):
        temp_num = self.num * other.den - self.den * other.num
        temp_den = self.den * other.den
        return f"{temp_num}/{temp_den}"

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return f"{temp_num}/{temp_den}"

    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return f"{temp_num}/{temp_den}"


x = Fraction(4,5)
print("x is ",x)
y = Fraction(2,3)
print("y is ",y)
z = x + y
print("addition of x + y is ", z)