def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in s.lower():
            return False
    return True


str = input("Enter String: ")

if is_pangram(str) is False:
    print("It is not a pangram")
if is_pangram(str) is True:
    print("It is a pangram")