a = 10
b = 5

def sum(a,b):
    return a+b


print(sum(a,b))
print(sum(20,15))

#default parameter

def greet(name="World"):
    print("Hello "+ name+ "!")

greet()
greet("Chetan")
