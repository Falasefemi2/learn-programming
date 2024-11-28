import time
import timeit
import cProfile
import math

def factorial_math(n):
    return math.factorial(n)

# Testing performance
n = 10000  # Test with a large number
start_time = time.time()  # Record the start time

result = factorial_math(n)  # Call your factorial function

end_time = time.time()  # Record the end time

# Calculate the time taken
execution_time = end_time - start_time

print(f"Factorial of {n} calculated successfully.")
print(f"Time taken: {execution_time:.6f} seconds")




start_time = time.time()

result = sum(range(1_000_000))

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")

execution_time = timeit.timeit("sum(range(1_000_000))", number=10)
print(f"Execution time for 10 runs: {execution_time:.5f} seconds")

def sample_function():
    total = 0
    for i in range(1_000_000):
        total += i
    return total
cProfile.run("sample_function()")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
cProfile.run("factorial(1000)")


# # Testing performance
# n = 10000  # Test with a large number
# start_time = time.time()  # Record the start time

# result = factorial(n)  # Call your factorial function

# end_time = time.time()  # Record the end time

# # Calculate the time taken
# execution_time = end_time - start_time

# print(f"Factorial of {n} calculated successfully.")
# print(f"Time taken: {execution_time:.6f} seconds")


