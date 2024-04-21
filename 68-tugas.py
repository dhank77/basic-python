# Exercise 68
# Write a function definition named only_even_numbers that takes in sequence of numbers and returns the even numbers in a list.

def only_even_numbers(data) : 
    even = []
    for x in data :
        if((x % 2) == 0) :
            even.append(x)
    return even

assert only_even_numbers([1, 2, 3]) == [2]
assert only_even_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-4, -2, 2, 4]
assert only_even_numbers([-4, -3, 1]) == [-4]
assert only_even_numbers([1, 1, 1, 1, 1, 1]) == []
print("Exercise 68 is correct.")