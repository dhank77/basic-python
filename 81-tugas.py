# Exercise 81
# Write a function definition named shortest_string that takes in a list of strings and returns the shortest string in the list.

def shortest_string(data) : 
    count = len(data[0])
    text = data[0]
    for x in data :
        if(len(x) < count) :
            text = x
    return text

assert shortest_string(["kiwi", "mango", "strawberry"]) == "kiwi"
assert shortest_string(["hello", "everybody"]) == "hello"
assert shortest_string(["mary", "had", "a", "little", "lamb"]) == "a"
print("Exercise 81 is correct.")