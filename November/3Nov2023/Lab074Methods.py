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

    def sleep(self, timing):
        print("sleep for "+ str(timing))

    def walk(self):
        return "I am walking " + self.name  # accessing attribute of class in method


chetan_obj = Person()
chetan_obj.name =  "CHetan"
print(chetan_obj.walk())
chetan_obj.sleep(5)
