import requests
import numpy as np


response = requests.get("https://api.github.com")
print(response.json())


# Create a 2D array
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])

print("2D Array:")
print(two_d_array)



# Create a 2D array filled with zeros
zeros_array = np.zeros((2, 3))  # 2 rows, 3 columns
print("2D Array of Zeros:")
print(zeros_array)
