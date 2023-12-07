class Atm:

    def __init__(self):
        self.pin = ""
        self. balance = 0
        print("id of self is ",id(self))
        self.menu()

    def menu(self):
        user_input = int(input("""
                                Hello How would you like to proceed 
                                1. Create pin
                                2. Deposit 
                                3. Withdraw
                                4. Check Balance
                                5. Exit
        """))

        if user_input == 1 :
            self.set_pin()
        elif user_input == 2 :
            self.deposit()
        elif user_input == 3 :
            self.withdraw()
        elif user_input == 4 :
            self.check_balance()
        else :
            print("BYE")

    def set_pin(self):
        self.pin = int(input(" Please set your pin"))

    def deposit(self):
        user_pin = int(input(" Enter your pin"))
        if user_pin == self.pin :
            amount = int(input("ENter amount to be deposited"))
            self.balance += amount
        else :
            print("Invalid Pin")

    def withdraw(self):
        user_pin = int(input(" Enter your pin"))
        if user_pin == self.pin :
            amount = int(input("Enter amount to be Withdrawn"))
            if amount <= self. balance:
                self.balance -= amount
            else:
                print("Low balance cannot withdraw the amount")
        else :
            print("Invalid Pin")

    def check_balance(self):
        user_pin = int(input(" Enter your pin"))
        if user_pin == self.pin :
            print("Your acccount balance is ", self.balance)
        else :
            print("Invalid Pin")


sbi = Atm()
print("the id of sbi object is ", id(sbi))      # the self and sbi will have same id when SBI object is created

hdfc = Atm()
print("the id of hdfc object is ", id(hdfc))

