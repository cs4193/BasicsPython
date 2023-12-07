with open("chetan.txt",'r') as file:
    content = file.read()
    print(content)
    file.close()

with open("chetan.txt", 'w') as file:
    file.write("No hello for you ")
    file.close()

with open("chetan.txt",'r') as file:
    content = file.read()
    print(content)
    file.close()

