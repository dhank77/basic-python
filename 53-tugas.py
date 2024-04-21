#  Exercise 53
# Write a function definition named forth that takes in sequence and returns the forth value of that sequence.

def forth(data) :
    return data[3]

assert forth("ubuntu") == "n"
assert forth([1, 2, 3, 4]) == 4
assert forth(["python", "is", "awesome", "right?"]) == "right?"
print("Exercise 53 is correct.")