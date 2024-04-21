# Exercise 15
# Write a function definition named is_even that takes in a number and returns True or False if that number is even.
import random
    
positive_even_number = random.randrange(2, 101, 2)
negative_even_number = random.randrange(-100, -1, 2)

positive_odd_number = random.randrange(1, 100, 2)
negative_odd_number = random.randrange(-101, 0, 2)

def is_even(number) : 
    if(number % 2) :
        return False
    else :
        return True

assert is_even(2) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(positive_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(positive_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(negative_odd_number) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(negative_even_number) == True, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 15 is correct.")