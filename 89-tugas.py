# Run this code to create data for the next two questions
book = {
    "title": "Genetic Algorithms and Machine Learning for Programmers",
    "price": 36.99,
    "author": "Frances Buontempo"
}

# Exercise 89
# Write a function named get_price that takes in a dictionary and returns the price

def get_price(data) :
    return data['price']

assert get_price(book) == 36.99
print("Exercise 89 is complete.")