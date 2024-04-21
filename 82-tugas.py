# Exercise 82
# Write a function definition named longest_string that takes in sequence of strings and returns the longest string in the list.

def longest_string(data) : 
    count = len(data[0])
    text = data[0]
    for x in data :
        if(len(x) > count) :
            text = x
    return text

assert longest_string(["kiwi", "mango", "strawberry"]) == "strawberry"
assert longest_string(["hello", "everybody"]) == "everybody"
assert longest_string(["mary", "had", "a", "little", "lamb"]) == "little"
print("Exercise 82 is correct.")