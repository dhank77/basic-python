# Exercise 57
# Write a function definition named first_and_second that takes in sequence and returns the first and second value of that sequence as a list

def first_and_second(data) :
    return [data[0], data[1]]

assert first_and_second([1, 2, 3, 4]) == [1, 2]
assert first_and_second(["python", "is", "awesome"]) == ["python", "is"]
assert first_and_second(["strawberry", "kiwi", "mango", "guava"]) == ["strawberry", "kiwi"]
print("Exercise 57 is correct.")