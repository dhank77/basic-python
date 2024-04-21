# Exercise 37
# Write a function definition named remainder that takes in two numbers and returns the remainder of first argument divided by the second argument.

def remainder(number1, number2) :
    return number1 % number2

assert remainder(3, 3) == 0
assert remainder(5, 2) == 1
assert remainder(7, 5) == 2
print("Exercise 37 is correct.")