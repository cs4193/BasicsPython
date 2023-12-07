# Public - Variable - Don't Mention anything
# Protected - _
# Private - __

# Variable and Function

class Person:

    def __init__(self,name, age):
        self.__name = None
        self.__age = None

    def get_name(self):     # public function is created to set provate variable in a class
        return self.__name

    def set_name(self,name):
        if name == "John":
            print("Cannot set this name")
        else:
            self.__name = name

    def print_details(self):
        print("your details are ", self.__name, self.__age)


chetan = Person("chetan", 30)
chetan.print_details()

print(chetan.get_name())

chetan.set_name("John")
