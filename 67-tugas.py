# Exercise 67
# Write a function definition named only_odd_numbers that takes in sequence of numbers and returns the odd numbers in a list.

def only_odd_numbers(data) : 
    odd = []
    for x in data :
        if((x % 2) == 1) :
            odd.append(x)
    return odd

assert only_odd_numbers([1, 2, 3]) == [1, 3]
assert only_odd_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -3, -1, 1, 3, 5]
assert only_odd_numbers([-4, -3, 1]) == [-3, 1]
assert only_odd_numbers([2, 2, 2, 2, 2]) == []
print("Exercise 67 is correct.")