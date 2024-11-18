def find_largest(numbers):
    if not numbers: # check if list is empty
        return None
    
    largest = numbers[0] # Assume first number is largest
    
    # Check each number against our current largest
    for number in numbers:
        if number > largest:
            largest = number
    return largest

num = [4,5,2,3,9,11,60]
result = find_largest(num)
print(f"The largest number is: {result}")


def find_smallest(numbers):
    if not numbers:
        return None
    
    smallest = numbers[0]
    
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest
num = [4,5,2,3,9,11,60, -1]
result = find_smallest(num)
print(f"The smallest number is {result}")

def find_smallest_biggest(numbers):
    if not numbers:
        return None
    
    smallest = numbers[0]
    largest = numbers[0]
    
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
            
    return smallest, largest

# Test Cases
def run_tests():
    test_cases = {
        "Test Case 1": ([3, 1, 4, 1, 5, 9, 2, 6]),
        "Test Case 2": ([10]),
        "Test Case 3": ([]),
        "Test Case 4": ([-5, -1, -10]),
        "Test Case 5": ([0, 0, 0]),
        "Test Case 6": ([1.5, 2.5, -3.5]),
        "Test Case 7": ([100, -100, 50]),
    }

    for name, input_data in test_cases.items():
        result = find_smallest_biggest(input_data)
        print(f"{name} with input {input_data} gives output: {result}")

# Run the tests
run_tests()


def find_twice(num, target):
    if not num:
        return 0
    
    count = 0
    
    for n in num:
        if n == target:
            count += 1
    return count

numbers = [1, 2, 2, 2, 3, 4]
target = 2
result = find_twice(numbers, target)
print(f"The number {target} appears {result} times")  # Should print: The number 2 appears 3 times

# More test cases
print(find_twice([], 5))          # Should print: 0
print(find_twice([1,1,1], 1))     # Should print: 3
print(find_twice([1,2,3,4], 5))   # Should print: 0
  
    
