import threading
import time 

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)
        
def print_letters():
    for letter in "ABCDE":
        print(f"Letter: {letter}")
        time.sleep(1)
        
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished executions")



# Function to print numbers from 1 to 10
def print_number_one_to_ten():
    for num in range(1, 11):  # Starts from 1 and ends at 10
        print(f"Number: {num}")
        time.sleep(1)

# Function to print the square of numbers from 1 to 10
def square_nums():
    for number in range(1, 11):  # Starts from 1 and ends at 10
        print(f"Square of {number}: {number ** 2}")  # Print the square
        time.sleep(1)

# Create threads
thread3 = threading.Thread(target=print_number_one_to_ten)
thread4 = threading.Thread(target=square_nums)

# Start threads
thread3.start()
thread4.start()

# Wait for threads to complete
thread3.join()
thread4.join()

print("Both threads have finished executing!")
