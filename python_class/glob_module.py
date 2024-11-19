# File Wildcards with glob Module
# The glob module is used to find files and directories matching a specified pattern. It’s very handy for tasks where you need to filter or list specific files based on their names or extensions.

# Topics to Cover:
# What is the glob module?
# Wildcard patterns (*, ?, [...]).
# Practical examples using glob.

# What is the glob Module?
# The glob module allows you to retrieve files and directories that match a specific pattern. Patterns are written using wildcards:

# *: Matches zero or more characters.
# ?: Matches exactly one character.
# [abc]: Matches any one of the characters inside the brackets.

# 2. Wildcard Patterns:
# Pattern	Example	Matches
# *.txt	Files ending with .txt	file.txt, notes.txt
# data?.csv	data1.csv, data2.csv	Files with one variable character after data
# [0-9]*	Files starting with numbers	123file.txt, 9data.log

import glob
import os


# # List all .txt files in the current directory
# txt_files = glob.glob("*.txt")
# print("Text files:", txt_files)

# # List all .csv files with a single-digit number in their name
# csv_files = glob.glob('test?.csv')
# print("CSV files:", csv_files)

# # List all Python files in the directory and subdirectories
# py_files = glob.glob("**/*.py", recursive=True)
# print("Python files:", py_files)

# os.mkdir("test_dir")
# os.chdir("test_dir")
# with open("example.txt", "w") as f:
#     f.write("This is a test file.")
  
# print(glob.glob("*.txt"))


def create_files():
    # Create .txt files
    with open("report1.txt", "w") as file:
        file.write("This is report 1.")
    with open("report2.txt", "w") as file:
        file.write("This is report 2.")

    # Create .csv files with actual data
    with open("data1.csv", "w") as file:
        file.write("Column1,Column2\nValue1,Value2")
    with open("data2.csv", "w") as file:
        file.write("Column1,Column2\nValue3,Value4")  # Writing meaningful data

    # List all .txt files
    txt_files = glob.glob("*.txt")
    print("TXT files:", txt_files)
    
    # Find files starting with 'data'
    data_files = glob.glob("data*.csv")  # Corrected pattern
    print("Data files:", data_files)
    
    # Recursively search for .csv files (you can adjust the pattern as needed)
    csv_files = glob.glob('**/*.csv', recursive=True)  # Adjusted to find all CSVs recursively
    print("CSV files:", csv_files)

# Call the function to create files and list them
create_files()


