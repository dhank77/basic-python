# Exercise 74
# Write a function definition named count_odds that takes in sequence of numbers and returns True if there are any odd numbers in the sequence

def count_odds(data) :
    count = 0
    for x in data :
        if(x % 2) :
            count += 1
    return count

assert count_odds([1, 2, 3]) == 2
assert count_odds([2, 5, 6]) == 1
assert count_odds([3, 3, 3]) == 3
assert count_odds([2, 4, 6]) == 0
print("Exercise 74 is correct.")