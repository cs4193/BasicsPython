def PalindrmeCheck(str):
    if str == str[::-1]:
        return True
    else:
        return False

user_input = input("Enter your string \n")

def reverse_string(str1):
    revstr = ""
    for i in str1:
        revstr = i + revstr
    return revstr
if user_input == reverse_string(user_input):
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")
print(PalindrmeCheck("naman"))