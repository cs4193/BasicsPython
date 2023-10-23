str = input("Enter the string \n").lower()
count = 0
for char in str:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count +=1
print(f"{str} has {count} vowels and {len(str)-count} consonants")
