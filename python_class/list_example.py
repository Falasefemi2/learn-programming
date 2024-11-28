import itertools

from functools import reduce

# Example: Sum of all numbers
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", total)

# Example: Using itertools
numbers = [1, 2, 3]
permutations = list(itertools.permutations(numbers))
print("Permutations:", permutations)

combinations = list(itertools.combinations(numbers, 2))
print("Combinations:", combinations)


# Example: Basic List Operations
numbers = [5, 2, 9, 1, 7]

numbers.append(10)    # Add an element
print("After append:", numbers)

numbers.pop()         # Remove the last element
print("After pop:", numbers)

numbers.sort()        # Sort the list
print("Sorted list:", numbers)


# Example: List Comprehension
squared = [x ** 2 for x in range(10)]
print("Squared numbers:", squared)

even_numbers = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", even_numbers)


# Example: Using map and filter
numbers = [1, 2, 3, 4, 5]

# Double each number
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled)

# Filter out odd numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# Example: Custom Sorting
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted by age:", sorted_students)


odd_nums = [x for x in range(20) if x % 2 != 0]
print("Odd Numbers:", odd_nums)

# Part 2: Process Even Numbers
nums = list(range(20))
even_nums = [x for x in nums if x % 2 == 0]
squared = [x ** 2 for x in even_nums]
sum_of_squares = sum(squared)

print("Even Numbers:", even_nums)
print("Squares of Even Numbers:", squared)
print("Sum of Squares:", sum_of_squares)

# Part 3: Find Combinations
nums_for_combination = [1, 2, 3, 4]
combination = list(itertools.combinations(nums_for_combination, 2))
print("Combinations:", combination)
