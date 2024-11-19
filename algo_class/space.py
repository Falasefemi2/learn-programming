# Module 1: Fundamentals
# Lecture 3: Space Complexity
# Space Complexity measures how much additional memory our code needs as input grows.

# 1. Types of Space:
def example(lst):    # lst is input space (we don't count this)
    x = 5           # constant space O(1)
    y = []          # auxiliary space (this we count)
    
# 2. Common Space Complexities:
# O(1) Space - Constant
def constant_space(n):
    x = 5
    y = 10
    z = x + y
    return z

# O(n) Space - Linear
def linear_space(n):
    result = []
    for i in range(n):
        result.append(i)  # list grows with input
    return result

# O(n²) Space - Quadratic
def quadratic_space(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    return matrix

# What is Space Complexity?
# Think of Space Complexity like packing boxes for moving:

# Like using the same box regardless of how much stuff you have

# Constant Space O(1)
def get_first_item(list_items):
    first = list_items[0]    # only need space for one item
    return first

# Like using one calculator regardless of numbers
def add_numbers(a, b):
    sum = a + b    # only need space for one sum
    return sum

# Linear Space O(n)
# Like needing one box for each item you have
def copy_items(items):
    new_list = []             # new list grows with input
    for item in items:
        new_list.append(item) # need space for each item
    return new_list

# Real-world example: If you have 5 books, you need 5 spaces
# If you have 10 books, you need 10 spaces

# Example 1: Constant Space O(1)
def count_items(items):
    count = 0                # only need one counter
    for item in items:
        count += 1
    return count

# Example 2: Linear Space O(n)
def double_items(items):
    doubled = []            # new list
    for item in items:
        doubled.append(item * 2)
    return doubled


# What storage is needed here?
def count_numbers(max_num):
    counter = 0             # Needs space for one number
    for num in range(max_num):
        if num % 2 == 0:    # Checking even numbers
            counter += 1
    return counter

# VS

def store_numbers(max_num):
    even_numbers = []       # Needs growing space
    for num in range(max_num):
        if num % 2 == 0:
            even_numbers.append(num)  # Adds more numbers
    return even_numbers

# Test with max_num = 6
count_numbers(6)
# Storage needed: just one number (counter)
# counter = 3 (for 0,2,4)

store_numbers(6)
# Storage needed: list storing [0,2,4]
# More numbers = More storage!
