def sort_words(s):
    words = s.split('-')
    words.sort()
    return '-'.join(words)

s = input("Enter String: ")

print(sort_words(s))
