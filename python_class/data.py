# Data Structures

# More on Lists
# Lists are one of Python's most powerful data structures. They are:

# Ordered
# Mutable (you can change their elements)
# Allow duplicate values

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])

# Modifying a list
fruits[1] = "blueberry"
print(fruits)

# Adding to a list
fruits.append("orange")
print(fruits)

# Removing from a list
fruits.remove("cherry")
print(fruits)

print(fruits[:2])

# List Comprehension: A concise way to create lists.
sqaures = [x**2 for x in range(1,6)]
print(sqaures)

# del Statement
# The del statement is used to delete elements from a list or even delete entire variables.
# Deleting a specific element
numbers = [10, 20, 30, 40]
del numbers[1]  
print(numbers)  # Output: [10, 30, 40]

# Deleting a slice
del numbers[:2]  
print(numbers)  # Output: [40]

# Deleting the entire list
del numbers  


# Tuples and Sequences
# Tuples are like lists, but they are immutable (cannot be changed). They are used for fixed collections of data.

# creating a tuple
coordinates = (10,20)

# accessing elements
print(coordinates[0])

# Tuples are immutable, so this will cause an error:
# coordinates[0] = 30  

# Tuple unpacking
x, y = coordinates
print(x, y)  # Output: 10 20


# Sets
# Sets are unordered collections of unique items. They are great for eliminating duplicates.

# creating a set
unique_numbers = {1,2,3,4}
print(unique_numbers)

# adding an element
unique_numbers.add(7)
print(unique_numbers)

# removing an element
unique_numbers.remove(2)
print(unique_numbers)


# Dictionaries
# Dictionaries store data in key-value pairs.

# creating a dictionary
person = {"name": "femi", "age": 24, "city": "Lagos"}
# accessing values
print(person["name"])
# adding a new key-value pair
person["profession"] = "Developer"
print(person)

# deleting a ket-value pair
del person["city"]
print(person)

# Looping Techniques
# Looping through a list
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
    
# Looping through a dictionary:
for key, value in person.items():
    print(f"{key}: {value}")
    
# Using enumerate to get index and value:
fruits = ["apple", "orange", "cherry"]
for index, fruit in enumerate(fruits):
    print(index,fruit)
    
# Comparing Sequences
# Python allows you to compare sequences (lists, tuples, etc.) lexicographically, using operators like <, <=, >, >=.

list1 = [1, 2, 3]
list2 = [1, 2, 4]
print(list1 < list2)  # Output: True (compares element by element)


# Exercises

# Odd Numbers Set
# Create a set containing all odd numbers from 1 to 20 and print it.

# Person Info Dictionary
# Create a dictionary with your name, age, and hobby. Add a key for your favorite programming language and print the dictionary.

# Tuple Unpacking
# Create a tuple with 5 numbers and unpack it into variables. Print each variable.

# Unique Words
# Write a program that takes a sentence, splits it into words, and stores unique words in a set.


odd_numbers = {set_num for set_num in range(1, 21) if set_num % 2 != 0}
print(odd_numbers)

        
person2 = {"name": "falase", "age": 12, "hobby": "dancing"}

person2["fav_lang"] = "Javascript"
print(person2)

numbers = (1, 2, 3, 4, 5)
a, b, c, d, e = numbers
print(a, b, c, d, e)

    
# Input a sentence from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words and store them in a set to keep only unique words
unique_words = set(sentence.split())

# Print the unique words
print("The unique words are:", unique_words)



