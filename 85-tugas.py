# Exercise 85
# Write a function definition named get_values_in_common that takes two lists and returns a single set with the values that each list has in common

def get_values_in_common(data1, data2) : 
    common = []
    for x in data1 :
        for y in data2 :
            if(x == y) :
                common.append(x)
    return set(common)

assert get_values_in_common([5, 1, 2, 3], [3, 4, 5, 5]) == {3, 5}
assert get_values_in_common([1, 2], [2, 2, 3]) == {2}
assert get_values_in_common(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"tomato"}
print("Exercise 85 is correct.")