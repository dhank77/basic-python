# Exercise 51
# Write a function definition named second that takes in sequence and returns the second value of that sequence.

def second(data) :
    return data[1]

assert second("ubuntu") == "b"
assert second([1, 2, 3]) == 2
assert second(["python", "is", "awesome"]) == "is"
print("Exercise 51 is correct.")