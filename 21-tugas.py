# Exercise 21
# Write a function definition named half that takes in a number and returns half the provided number.

import random
    
positive_even_number = random.randrange(2, 101, 2)
negative_even_number = random.randrange(-100, -1, 2)

positive_odd_number = random.randrange(1, 100, 2)
negative_odd_number = random.randrange(-101, 0, 2)

def half(number) :
    return number / 2

assert half(4) == 2
assert half(5) == 2.5
assert half(positive_odd_number) == positive_odd_number / 2
assert half(positive_even_number) == positive_even_number / 2
assert half(negative_odd_number) == negative_odd_number / 2
assert half(negative_even_number) == negative_even_number / 2
print("Exercise 21 is correct.")