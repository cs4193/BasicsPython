myDict = {}
myDict2 = dict()

print(type(myDict))
print(type(myDict2))

phoneBook = {"Batman" : 98763739, "Superman" : 1237010, "Wonder" : 1294101}
print(phoneBook)
print(len(phoneBook))
print(phoneBook["Batman"])
print(phoneBook["Wonder"])

phoneBook2 = dict(Batman= 123, Cersi= 12311, GB= 2131)
print(phoneBook2["GB"])
print(phoneBook2.get('Cersi'))

new_dic = dict(name = "pramod", age = 34, isMale = True, address = "KA")
print(new_dic)
print(new_dic["age"])
print(new_dic.get("isMale"))
print(new_dic.values())     # returns all the values