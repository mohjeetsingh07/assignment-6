str = input("Enter String: ")
str1 = str.lower()

def palindrome(str1):
    return str1 == str1[::-1]

if palindrome(str1):
    print(str + " is a palindrome")
else:
    print(str + " is not a palindrome")
