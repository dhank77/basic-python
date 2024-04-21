# Exercise 10
# Write the code necessary to produce a single list that holds all fruits then all vegetables in the order as they were sorted above.

fruits = ["mango", "banana", "guava", "kiwi", "strawberry", "tomato"]
fruits.sort(reverse = True)
vegetables = ["eggplant", "broccoli", "carrot", "cauliflower", "zucchini", "tomato"]
vegetables.sort()
fruits_and_veggies = fruits + vegetables

assert fruits_and_veggies == ['tomato', 'strawberry', 'mango', 'kiwi', 'guava', 'banana', 'broccoli', 'carrot', 'cauliflower', 'eggplant', 'tomato', 'zucchini']
print("Exercise 10 is correct")