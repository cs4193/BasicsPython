'''%s is used for strings
    %i is used for integers
    %f is used for float values'''

str3 = "%i + %i = %i" % (1,2,3)
print(str3)     # 1 + 2 = 3

str4 = "%f" %(1.11)
print(str4)     # 1.110000

str5 = "%.3f" %(1.2345)
print(str5)    # 1.234

str = "i like %s" %"Python"
print(str)      # i like Python

str1 = "Chetan"
str2 = "Hello %s" % str1
print(str2)     # Hello Chetan

name = input("Enter your first name \n")
lastname = input("Enter your last name\n")
print("Hello %s %s" %(name, lastname))      # Hello Chetan Shetty
