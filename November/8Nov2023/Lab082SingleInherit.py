# Parent - Child
# Father -> son

# single inheritance

class Parent:
    bank_bal = 1000
    def house(self):
        print("this house is owned by Father")

    def money(self):
        print("this is fathers money")

class Son(Parent):

    def company(self):
        print("this is sons company")


chetan = Son()
chetan.house()  # child class object inheriting the parent class methods
chetan.money()
print(chetan.bank_bal)      # child class object inheriting the parent class attributes
chetan.company()    # child class object keeping its own methods