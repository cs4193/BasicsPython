class BankAccount:

    def __init__(self):
        self.openbalance = 0        # instance variable
        self.__balance = 0
        self.__private_var = 100    # private variable

    def deposit(self,amount):       # public method
        self.__balance += amount

    def _withdraw(self,amount):     # protected  method
        self.__balance -= amount

    def __show_balance(self):
        print("your balance is ", self.__balance)

    def IS_Auth_True_show_bal(self, isAuth):    # creating a public method to access private
        if isAuth:
            self.__show_balance()
        else:
            print("You are not Auth")

    def do_withdraw_by_bank_manager(self, amount):      # creating a public method to access protective method
        self._withdraw(amount)


sbi = BankAccount()
print(sbi.openbalance)
sbi.deposit(1000)
sbi.IS_Auth_True_show_bal(True)
sbi._withdraw(499)      # protected can be accessed like this but not a good practice
sbi.IS_Auth_True_show_bal(True)
sbi.IS_Auth_True_show_bal(False)
sbi.do_withdraw_by_bank_manager(100)
sbi.IS_Auth_True_show_bal(True)


# how to access private variable using a bad hack in python
#sbi._BankAccount__private_var = 10
print(sbi._BankAccount__private_var)

