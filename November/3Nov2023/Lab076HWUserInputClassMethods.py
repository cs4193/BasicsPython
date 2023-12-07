class Person:
    # Attributes
    name = None
    age = None
    address = None

    # Methods
    def details(self):
        print(f"Hello {self.name}   your age is {self.age} and you live in {self.address} ")


obj_person1 = Person()
obj_person2 = Person()
name_person1 = input("Enter the name of first person ")
age_person1 = input("Enter the age of first person ")
address_person1 = input("Enter the address of first person ")

obj_person1.name = name_person1
obj_person1.age = age_person1
obj_person1.address = address_person1
obj_person1.details()

name_person2 = input("Enter the name of second person ")
age_person2 = input("Enter the age of second person ")
address_person2 = input("Enter the address of second person ")

obj_person2.name = name_person2
obj_person2.age = age_person2
obj_person2.address = address_person2
obj_person2.details()


