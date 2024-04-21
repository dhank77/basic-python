# Exercise 62
# Write a function definition named median that takes in sequence of numbers and returns the average value
def median(data) :
    if(len(data) % 2) :
        return data[len(data) // 2]
    else :
        return sum(data) / len(data)

assert median([1, 2, 3, 4, 5]) == 3.0
assert median([1, 2, 3]) == 2.0
assert median([1, 5, 6]) == 5.0
assert median([1, 2, 5, 6]) == 3.5
print("Exercise 62 is correct.")