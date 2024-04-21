# Exercise 63
# Write a function definition named mode that takes in sequence of numbers and returns the most commonly occuring value

def mode(data) :
    count = 0
    numb = data[0]

    for i in data :
        check = data.count(i)
        if(check > count) :
            count = check
            numb = i

    return numb

assert mode([1, 2, 2, 3, 4]) == 2
assert mode([1, 1, 2, 3]) == 1
assert mode([2, 2, 3, 3, 3]) == 3
print("Exercise 63 is correct.")