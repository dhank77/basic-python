# Exercise 46
# Write a function definition named remove_vowels that takes in string and returns the string without any vowels

def remove_vowels(argumen) : 
    letter = ['a', 'e', 'i', 'o', 'u']
    count = ''
    for x in argumen :
        if((x in letter) == False) :
            count += x
    return count

assert remove_vowels("banana") == "bnn"
assert remove_vowels("ubuntu") == "bnt"
assert remove_vowels("mango") == "mng"
assert remove_vowels("QQQQ") == "QQQQ"
print("Exercise 46 is correct.")