# Exercise 84
# Write a function definition named get_unique_values_from_two_lists that takes two lists and returns a single set with only the unique values

def get_unique_values_from_two_lists(data1, data2) :
    # shorthand
    # return set(data1) | set(data2)
    
    return set(data1).union(set(data2))

assert get_unique_values_from_two_lists([5, 1, 2, 3], [3, 4, 5, 5]) == {1, 2, 3, 4, 5}
assert get_unique_values_from_two_lists([1, 1], [2, 2, 3]) == {1, 2, 3}
assert get_unique_values_from_two_lists(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"tomato", "mango", "kiwi", "eggplant", "broccoli"}
print("Exercise 84 is correct.")