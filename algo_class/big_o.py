# Module 1: Fundamentals
# Lecture 2: Big O Notation
#  Big O Notation is how we measure the efficiency of our code - specifically how it performs as the input gets larger.
#  1. Why Big O Matters
#  Let's look at two ways to sum numbers from 1 to n:

# Method 1: Using a loop - O(n)
def sum_loop(n):
    total = 0
    for i in range(1, n +1):
        total += i
    return total

# Method 2: Using formula - O(1)
def sum_formula(n):
    return (n * (n + 1)) //2

# When n = 5, both work fine
# When n = 1,000,000, Method 2 is MUCH faster!

# 2. Common Big O Notations (from fastest to slowest):
# O(1) - Constant Time

# No matter the size of input, takes same time
def get_first(lst):
    if not lst: return None
    return lst[0]

# O(log n) - Logarithmic Time
# Binary Search example
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n) - Linear Time
# Time grows linearly with input size
def find_max(lst):
    if not lst: return None
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

# O(n²) - Quadratic Time
# Nested loops = quadratic time
def print_pairs(lst):
    for i in lst:
        for j in lst:
            print(i, j)
            
# Let me help explain how to determine Big O notation step by step!
# How to Determine Big O:

# Look at the code structure
# Count how many times we go through the data
# Consider how operations grow with input size

# Let's solve the practice problems together:

# Function 1
def func1(lst):
    return len(lst)

# How to analyze:

# Just gets length once
# No loops
# Always one operation regardless of list size
# Therefore: O(1) constant time

# Function 2
def func2(lst):
    for i in lst:     # One loop through list
        print(i)      # Does twice for each element
        print(i)
        
# How to analyze:

# One loop through list
# Each element printed twice, but still one pass through list
# If list has n elements, we do n * 2 operations
# Still: O(n) linear time (constants like 2 are dropped)

# Function 3
def func3(lst):
    for i in lst:         # Outer loop
        for j in lst:     # Inner loop
            if i == j:    # Comparison
                print("Match!")
                
# How to analyze:

# Has nested loops (one inside another)
# For each element (outer loop), we go through all elements again (inner loop)
# If list has n elements: n * n = n² operations
# Therefore: O(n²) quadratic time


# Simple Rules to Remember:

# No loops or recursion = O(1)
def example1(lst):
    return lst[0]  # O(1)

# One loop = O(n)
def example2(lst):
    for x in lst:  # O(n)
        print(x)
        
# Nested loops = O(n²)
def example3(lst):
    for x in lst:      # Outer loop
        for y in lst:  # Inner loop
            print(x,y) # O(n²)
            

def mystery(lst):
    print(lst[0])          # Line 1
    for x in lst:          # Line 2
        print(x)           # Line 3
    for i in lst:          # Line 4
        print(i)           # Line 5

# Can you try to determine its Big O? Think about:

# Are there nested loops?
# How many separate loops are there?
# Any constant time operations?

def mysterys(lst):
    print(lst[0])          # O(1) - constant time operation
    for x in lst:          # First loop: O(n)
        print(x)
    for i in lst:          # Second loop: O(n)
        print(i)
# Total Time Analysis:

# O(1) + O(n) + O(n)
# = O(1) + O(2n)
# = O(n)

# Why O(n)?

# Even though we have 2 loops, they're not nested
# We drop constants (the 2 in 2n)
# We drop less significant terms (the +1)
# We focus on the most significant term: n

def new_mystery(lst):
    total = 0                  # Line 1
    for i in lst:              # Line 2
        total += i             # Line 3
        for j in range(10):    # Line 4
            print("Hello")     # Line 5
    return total               # Line 6

def new_mysteryss(lst):
    total = 0                  # O(1)
    for i in lst:              # O(n)
        total += i             # O(1)
        for j in range(10):    # Important: this is O(10), not O(n)!
            print("Hello")     # O(1)
    return total               # O(1)

# ✓ Yes, there is a nested loop
# ✓ Correct! Inner loop is NOT dependent on input size (always 10 iterations)
# ❌ Actually, this is O(n), not O(n²)!

# Why O(n)?

# Though we have nested loops, the inner loop is CONSTANT (always 10)
# For each element in lst (n times):

# We do 10 operations


# So it's really n * 10 operations
# We drop constants (10)
# Final complexity: O(n)

