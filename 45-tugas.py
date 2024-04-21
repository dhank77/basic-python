# Exercise 45
# Write a function definition named count_vowels that takes in value and returns the count of the nubmer of vowels in a sequence.

def count_vowels(argumen) : 
    letter = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for x in argumen :
        if(x in letter) :
            count += 1
    return count

assert count_vowels("banana") == 3
assert count_vowels("ubuntu") == 3
assert count_vowels("mango") == 2
assert count_vowels("QQQQ") == 0
assert count_vowels("wyrd") == 0
print("Exercise 45 is correct.")