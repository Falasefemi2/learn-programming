age = 234

if age < 18:
    print("You are a minor")
elif age == 18:
    print("Congratulations on becoming an adult!")
else:
    print("You are a adult")
    

# Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I love", fruit)
    
# Iterating through a string
for letter in "Python":
    print(letter)
    
# Using `range()`
for number in range(5):
    print(number)
    
# The range() function generates a sequence of numbers.
# range(start, stop, step)
for i in range(5):
    print(i)
    
for i in range(1, 6):
    print(i)
    
for i in range(0,10,2): #even numbers from 0 to 8    
    print(i)
    
# break and continue
# break: Exits the loop prematurely
# continue: Skips the current iteration and continues to the next

for num in range(10):
    if num == 5:
        break # Stops the loop when num is 5
    print(f"break: {num}")

for num in range(10):
    if num % 2 == 0:
        continue # Skips even numbers
    print(f'continue: {num}')
    
if True:
    pass  # Do nothing for now
print("This code runs without error.")


# Defining Functions
# Functions allow you to group reusable code into a single block.

def function_name(parameters):
    # Code block
    return value  # Optional

# function without no parameters
def greet():
    print("Hello World")

# functions with parameters
def add_numbers(a, b):
    return a + b   
 
# Call the functions
greet()
result = add_numbers(5, 4)
print(f"The sum is: {result}") 

# More on Defining Functions
# Functions can have default parameters and keyword arguments.
def introduce(name, age=18): # Default age is 18
    print(f"My name is {name} and I am {age} years old.")
    
introduce("Femi")
introduce("Femi", 25)


def check_nums(nums):
    if nums > 0:
        return "Positive"
    elif nums < 0:
        return "Negative"
    else:
        return "Zero"
    
result = check_nums(0)
print(f"The result is {result}")

for i in range(1, 21):
    if i % 2 != 0:
        print(i)
        
def square(number):
    return number * number  # Multiplying the number by itself


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(is_even(8))

for i in range(3,31, 3):
    print(i)

    