# Run this cell in order to have some setup data for the next exercises
books = [
    {
        "title": "Genetic Algorithms and Machine Learning for Programmers",
        "price": 36.99,
        "author": "Frances Buontempo"
    },
    {
        "title": "The Visual Display of Quantitative Information",
        "price": 38.00,
        "author": "Edward Tufte"
    },
    {
        "title": "Practical Object-Oriented Design",
        "author": "Sandi Metz",
        "price": 30.47
    },
    {
        "title": "Weapons of Math Destruction",
        "author": "Cathy O'Neil",
        "price": 17.44
    }
]
# Exercise 93
# Write a function named get_average_book_price that takes in a list of dictionaries and returns the average book price.

def get_average_book_price(data) :
    price = []
    for x in data  :
        price.append(x['price'])
    return sum(price) / len(price)

assert get_average_book_price(books) == 30.725
print("Exercise 93 is complete.")