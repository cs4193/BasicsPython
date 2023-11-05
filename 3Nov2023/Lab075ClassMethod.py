class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

    def start_engine(self):
        print("starting engine")

    def drive(self):
        print("drive")

    def brake(self):
        print("brake")

    def who_is_driving(self):
        print("i am driving "+ self.name)

    def car_is_sold(self, owner, loc):
        print("the new owner of car is "+owner + loc)




tesla = Car()       # this is an instance of a class -object
lambo = Car()
tesla.name = "Tesla"
lambo.name = "Lamborgini"
tesla.who_is_driving()
lambo.who_is_driving()
tesla.car_is_sold("chetan","Pune")