# Exercise 79
# Write a function definition named only_negative_evens that takes in sequence of numbers and returns a list containing all the negative even numbers from the sequence

def only_negative_evens(data) : 
    negative = []
    for x in data :
        if((x % 2 == 0) and x < 0) :
            negative.append(x)
    return negative

assert only_negative_evens([1, -2, 3]) == [-2]
assert only_negative_evens([2, -5, -6]) == [-6]
assert only_negative_evens([3, 3, 4, 6]) == []
assert only_negative_evens([-2, 3, 4, -1, -4]) == [-2, -4]
print("Exercise 79 is correct.")