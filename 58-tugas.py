# Exercise 58
# Write a function definition named first_and_last that takes in sequence and returns the first and last value of that sequence as a list

def first_and_last(data) :
    return [data[0], data[len(data)-1]]

assert first_and_last([1, 2, 3, 4]) == [1, 4]
assert first_and_last(["python", "is", "awesome"]) == ["python", "awesome"]
assert first_and_last(["strawberry", "kiwi", "mango", "guava"]) == ["strawberry", "guava"]
print("Exercise 58 is correct.")