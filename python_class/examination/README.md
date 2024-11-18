<!-- @format -->

# Midterm Project: Student Management System

We will build a Student Management System where you can:

1 Add students.

2 Display all students.

3 Search for a student by name.

4 Save student data to a file.

5 Load student data from a file.

# Project Requirements

You will use the following concepts from the chapters we've covered:

1. Variables and Data Types: Storing student data.
2. Control Flow: Adding, searching, and displaying students.
3. Functions: Modularizing the code for specific tasks.
4. Loops: Iterating through students.
5. Data Structures: Using lists and dictionaries to store student data.
6. Modules: Importing built-in modules like os.
7. File Handling: Saving and loading student data from a file.
8. Object-Oriented Programming (OOP): Representing students as objects with attributes and methods.

# Project Outline

1. Define a Class for Students

class Student:
def **init**(self, name, age, school, grade):
self.name = name
self.age = age
self.school = school
self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, School: {self.school}, Grade: {self.grade}"

2. Define Functions for System Features

Add Student: Collect input, create a Student object, and add it to a list.
Display Students: Loop through the list and print each student.
Search Student: Search for a student by name.
Save Data: Write the student list to a file.
Load Data: Read student data from a file and populate the list.

3. Build the Menu System
   Create a loop to allow users to select features from a menu.
