# Error Handling
# Why Error Handling?
# Errors can occur while running a program. For example:

# Dividing by zero.
# Accessing a file that doesn’t exist.
# Inputting invalid data.
# If we don't handle errors, the program crashes. Error handling allows us to manage such situations and keep the program running.

# Basic Error Handling with try and except
# try:
    # code that might raise an error
    # risky_code()
# except ErrorType:
    # code to handle the error
    # print("An error occurred!")
    
# Handling Division by Zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
    
# Using else and finally
# else: Runs if no exceptions occur.
# finally: Runs no matter what, even if an exception is raised.
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a number")
else:
    print(f"You entered {number}")
finally:
    print("Program execution completed")

# Raising Exceptions
# You can raise your own exceptions using raise.
age = 5
if age < 0:
    raise ValueError("Age cannot be negative!")

# Custom Exception Classes
# You can create your own exceptions by inheriting from the Exception class.

class NegativeAgeError(Exception):
    pass

try:
    age = -3
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
except NegativeAgeError as e:
    print(e)
    
    

# Your Turn: Exercises
# Divide Safely: Write a program that:

# Takes two numbers as input.
# Handles division by zero and invalid input gracefully.
# File Handling Errors:

# Try opening a file that doesn’t exist.
# Catch the exception and print a friendly message.
# Custom Exceptions:

# Create a custom exception called InvalidNameError if a user enters a name shorter than 3 characters.
# Prompt the user for a name, validate it, and raise the exception if necessary.

def divide_safely():
    try:
        num1 = float(input("Enter the first value: "))
        num2 = float(input("Enter the second value: "))
        result = num1 / num2
        print(f"The result is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numeric values.")

divide_safely()

import os

filename = "texts.txt"

try:
    if os.path.exists(filename):
        with open(filename, "r") as file:
            contents = file.read()
            print(contents)
    else:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
except FileNotFoundError as e:
    print(e)
    
class InvalidNameError(Exception):
    pass

def validate_name():
    try:
        name = input('Enter your name: ')
        if len(name) < 3:
            raise InvalidNameError("Name must be at least 3 characters long.")
        print(f"Hello, {name}")
    except InvalidNameError as e:
        print(e)
validate_name()