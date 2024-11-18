# Modules
# Modules in Python are reusable pieces of code that you can import and use in your programs. They help organize your code into manageable sections and enable code reusability.

# Lesson 1: Importing Modules
# What is a Module?

# A file containing Python definitions and statements.
# File ends with .py (e.g., mymodule.py).
# How to Import Modules:

# Use the import statement to include a module in your program.

# Import the math module
import math

# Use a function from the math module
print(math.sqrt(16))  # Output: 4.0


# Lesson 2: Using Specific Functions
# You can import specific functions from a module:

from math import pi, sqrt

print(pi)           # Output: 3.141592653589793
print(sqrt(25))     # Output: 5.0

# Lesson 3: Aliases
# Modules or functions can be given aliases for convenience:
import math as m

print(m.sqrt(64))  # Output: 8.0


import mymodule
print(mymodule.greet('Falase'))


# Your Exercise
# Part 1: Built-in Modules
# Import the math module and:

# Find the square root of 144.
# Find the value of cos(0).
# Import the random module and:

# Generate a random integer between 1 and 10.
# Part 2: Custom Module
# Create your own module with a function that takes two numbers and returns their product.
# Import and use your custom module in another program.

import math

print(math.sqrt(144))
print(math.cos(0))

import random

print(random.randint(1, 10))

import mymodule
print(mymodule.two_numbers(2,10))