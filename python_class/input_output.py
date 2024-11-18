# Input and Output
# This chapter focuses on:

# Interacting with users via input and output.
# Working with files for reading and writing data.

# Lesson 1: Basic Input and Output
# Getting Input from the User:

# Use the input() function to collect data from the user.

name = input("Enter your name: ")
print(f"Hello, {name}!")

# Formatting Output:
# Use print() with formatted strings (f-strings) for dynamic output.
age = 25
print(f"I am {age} years old.")  # Output: I am 25 years old.

# Reading and Writing Files
# Writing to a File:

# Use the open() function with mode 'w' to write to a file.
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file!")
    
# Reading from a File:

# Use the open() function with mode 'r' to read from a file.

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a File:

# Use mode 'a' to add content to an existing file.
with open("example.txt", "a") as file:
    file.write("\nThis line is appended")

# File Iteration
# You can iterate over lines in a file using a loop:
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())



# Your Exercise
# Part 1: Basic Input/Output
# Write a program that:
# Asks the user for their favorite food.
# Prints a message saying, "Your favorite food is <food>".
# Part 2: File Operations
# Write a program to:
# Create a file called data.txt.
# Write the numbers from 1 to 10, each on a new line, into the file.
# Read the contents of the file and print them line by line.

fav_food = input("Your favorite food is: ")
print(f"Your favorite food is {fav_food}")

with open("data.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

    
with open("data.txt", "r") as file:
    contents = file.read()
    print(contents)
