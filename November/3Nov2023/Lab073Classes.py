# Class and object

# Class Person
# Attributes - name, age , phone no, height weight, gender, profession
# methods - can do-> run(), sleep(), sing(), talk(), learn(), fight(), think()

class Person:
    # Attributes
    name = None
    age = None
    phone_n = None
    height = None
    weight = None
    gender = None
    profession = None   # if value is not assigned to variable u cannot use it

    # Methods
    def talk(self):
        print("talk")

    def sleep(self):
        print("sleep")

    def walk(self):
        return "I am walking"


chetan_obj = Person()
chetan_obj.name = "Chetan"
chetan_obj.age = 30
chetan_obj.phone_n = "393710273"

print(chetan_obj)   # this will print address of the object

chetan_obj.sleep()

akshu_obj = Person()
akshu_obj.name = "Akshatha"
print(akshu_obj)
