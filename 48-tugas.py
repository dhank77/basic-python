# Exercise 48
# Write a function definition named ends_with_vowel that takes in string and True if the string ends with a vowel

def ends_with_vowel(argumen) :
    letter = ['a', 'e', 'i', 'o', 'u']
    if(argumen[len(argumen) - 1] in letter) :
        return True
    else :
        return False

assert ends_with_vowel("ubuntu") == True
assert ends_with_vowel("banana") == True
assert ends_with_vowel("mango") == True
assert ends_with_vowel("spinach") == False
print("Exercise 48 is correct.")