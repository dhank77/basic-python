# Exercise 44
# Write a function definition named has_vowels that takes in value and returns True if the string contains any vowels.

def has_vowels(argumen) : 
    letter = ['a', 'e', 'i', 'o', 'u']
    for x in letter :
        if(x in argumen) :
            return True

    return False
    
assert has_vowels("banana") == True
assert has_vowels("ubuntu") == True
assert has_vowels("QQQQ") == False
assert has_vowels("wyrd") == False
print("Exercise 44 is correct.")