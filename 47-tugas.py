# Exercise 47
# Write a function definition named starts_with_vowel that takes in string and True if the string starts with a vowel

def starts_with_vowel(argumen) :
    letter = ['a', 'e', 'i', 'o', 'u']
    if(argumen[0] in letter) :
        return True
    else :
        return False

assert starts_with_vowel("ubuntu") == True
assert starts_with_vowel("banana") == False
assert starts_with_vowel("mango") == False
print("Exercise 47 is correct.")