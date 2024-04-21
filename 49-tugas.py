# Exercise 49
# Write a function definition named starts_and_ends_with_vowel that takes in string and returns True if the string starts and ends with a vowel

def starts_and_ends_with_vowel(argumen) : 
    letter = ['a', 'e', 'i', 'o', 'u']
    if(argumen[len(argumen) - 1] in letter and argumen[0] in letter) :
        return True
    else :
        return False

assert starts_and_ends_with_vowel("ubuntu") == True
assert starts_and_ends_with_vowel("banana") == False
assert starts_and_ends_with_vowel("mango") == False
print("Exercise 49 is correct.")