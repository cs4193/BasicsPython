class Customer:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender


def greet(customer):
    print(id(customer))
    if customer.gender == "Male":
        print("Hello "+customer.name+ "Sir")
    else:
        print("Hello "+customer.name+ " ma'am")
    customer.name = "Akshatha"
    print(id(customer))
    cust = Customer("Chetan","Male")
    return cust


cust2 = Customer("akshu","Female")
print(id(cust2))        # reference variable here and passed in function point at same memeory location
new_cust1 = greet(cust2)
print(new_cust1.name)
print(cust2.name)   # after passing the reference of object the attribute of class was changed in the referenced


