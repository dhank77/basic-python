# Exercise 31
# Write a function definition named cube that takes in a number and returns the number times itself, times itself.
import random
    
positive_even_number = random.randrange(2, 101, 2)
positive_odd_number = random.randrange(1, 100, 2)

# def cube (number) :
#     return number * number * number

def cube (number) :
    return number ** 3

assert cube(3) == 27
assert cube(2) == 8
assert cube(5) == 125
assert cube(positive_odd_number) == positive_odd_number * positive_odd_number * positive_odd_number
print("Exercise 31 is correct.")