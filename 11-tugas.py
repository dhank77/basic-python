# Exercise 11
# Write a function definition for a function named add_one that takes in a number and returns that number plus one.

import random
    
positive_even_number = random.randrange(2, 101, 2)
negative_odd_number = random.randrange(-101, 0, 2)

def add_one(number) :
    return number + 1

    
assert add_one(2) == 3, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(0) == 1, "Zero plus one is one."
assert add_one(positive_even_number) == positive_even_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
assert add_one(negative_odd_number) == negative_odd_number + 1, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 11 is correct.") 