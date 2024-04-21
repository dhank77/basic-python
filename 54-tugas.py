# Exercise 54
# Write a function definition named last that takes in sequence and returns the last value of that sequence.

def last(data) :
    return data[len(data)-1]

assert last("ubuntu") == "u"
assert last([1, 2, 3, 4]) == 4
assert last(["python", "is", "awesome"]) == "awesome"
assert last(["kiwi", "mango", "guava"]) == "guava"
print("Exercise 54 is correct.")