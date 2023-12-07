class Variables:
    public_var = None
    _protected_var = None
    __private_var = None


obj1 = Variables()
obj1.public_var = "10"
print(obj1.public_var)
obj1._protected_var = 20        # The protected variables can be accessed but is not a good method to do
print(obj1._protected_var)
obj1.__private_var      # this will throw error as private variable cannot be accessed outside Class
