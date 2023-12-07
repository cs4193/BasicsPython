with open("Readline.txt",'r') as file:
    content = file.read()
    print(content)
    file.close()

print("**************using readline***********************")
with open("Readline.txt",'r') as file:
    content = file.readline()
    print(content)
    file.close()


print("**************using readlines***********************")
with open("Readline.txt",'r') as file:
    content = file.readlines()
    print(content)
    file.close()