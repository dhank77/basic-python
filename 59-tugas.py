# Exercise 59
# Write a function definition named first_to_last that takes in sequence and returns the sequence with the first value moved to the end of the sequence.

def first_to_last(data) :
    x = data[0]
    del data[0]
    data.append(x)
    return data

assert first_to_last([1, 2, 3, 4]) == [2, 3, 4, 1]
assert first_to_last(["python", "is", "awesome"]) == ["is", "awesome", "python"]
assert first_to_last(["strawberry", "kiwi", "mango", "guava"]) == ["kiwi", "mango", "guava", "strawberry"]
print("Exercise 59 is correct.")