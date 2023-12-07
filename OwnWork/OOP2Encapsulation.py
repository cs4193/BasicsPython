class Atm:

    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        print("id of self is ",id(self))
        self.__menu()

    def __menu(self):
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

    def get_pin(self):
        return self.__pin

    def set_pin(self,pin):
        #pin = input(" Please set your pin")
        if type(pin) == int:
            self.__pin = pin
            print("pin changed successfully")
        else:
            print("Incorrect pin ")

    def deposit(self):
        user_pin = int(input(" Enter your pin"))
        if user_pin == self.__pin :
            amount = int(input("ENter amount to be deposited"))
            self.__balance += amount
        else :
            print("Invalid Pin")

    def withdraw(self):
        user_pin = int(input(" Enter your pin"))
        if user_pin == self.__pin :
            amount = int(input("Enter amount to be Withdrawn"))
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Low balance cannot withdraw the amount")
        else :
            print("Invalid Pin")

    def check_balance(self):
        user_pin = int(input(" Enter your pin"))
        if user_pin == self.__pin:
            print("Your account balance is ", self.__balance)
        else :
            print("Invalid Pin")


sbi = Atm()
print("the id of sbi object is ", id(sbi))      # the self and sbi will have same id when SBI object is created
print(sbi.get_pin())
hdfc = Atm()
print("the id of hdfc object is ", id(hdfc))
hdfc.set_pin(2345)
hdfc.set_pin("5")
