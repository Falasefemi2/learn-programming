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

Project Title: Student Course Management System
Objective
Create a Python program that simulates a simple student course management system. The program should handle the following functionalities:

Register students.
Enroll students in courses.
Manage course data (add, update, delete courses).
View reports of students and courses.
Features to Implement

1. Basic Setup (Introduction & Data Types)
   Create a welcome message and provide options for the user (e.g., register, enroll, manage courses).
   Use appropriate data types for storing student details, courses, and enrollment data.
2. Control Flow
   Use if-elif-else statements to handle menu options.
   Use loops to allow users to perform multiple actions until they choose to exit.
3. Functions
   Write functions for:
   Registering students.
   Enrolling in a course.
   Adding, updating, and deleting courses.
   Viewing reports.
4. Data Structures
   Store students and courses in dictionaries. Example:
   students = {1: {"name": "Alice", "age": 20}}
   courses = {"CS101": {"title": "Intro to Computer Science", "credits": 3}}
   enrollments = {1: ["CS101"]}
5. Modules
   Use the random module to generate unique student IDs or course codes.
6. File Handling
   Save all data (students, courses, enrollments) to a file.
   Load data from the file when the program starts.
7. OOP (Optional)
   Create Student and Course classes to represent these entities.
8. Error Handling
   Handle errors like:
   Trying to enroll a non-existent student in a course.
   Adding duplicate courses.
   Invalid inputs.
9. API Integration (Optional)
   Fetch some course details (e.g., from a free API like jsonplaceholder.typicode.com) and display them.
10. Operating System
    Use os to create a folder to store saved files for the system.
    Check if the folder already exists.
11. File Wildcards
    Use the glob module to display all saved files related to students and courses.
    Expected Deliverables
    A functional Python program.
    Outputs formatted clearly for users.
    Files created for persistent data storage.
    Extra Challenge
    Add a feature to calculate the total credits a student is enrolled in and display the result.

Task Management System
Project Description:
Build a simple system where users can:

Add tasks with details like title, description, and due date.
Mark tasks as completed.
View all tasks or only completed/incomplete tasks.
Save and load tasks from a file.
Key Features:
Task Addition: Add tasks with a title, description, and due date.
Mark Completion: Update task status to "completed."
Filter Tasks: View all tasks or filter by completion status.
File Persistence: Save tasks to a file and load them back when restarting the program.
Hints for Implementation:
Define a Task Class:

Attributes: title, description, due_date, completed (boolean).
Method: mark_completed() to update the task status.
Create a task_list:

Store all tasks added by the user.
Functions to Implement:

add_task(): Add a new task to the list.
view_tasks(): Display tasks with options to filter.
mark_task_completed(): Update a task's status.
save_tasks(): Save all tasks to a file.
load_tasks(): Load tasks from a file.
Use File Operations:

Use a file like tasks.txt to store task data.
Menu-Driven Interface:

Provide a menu for user interaction with options like adding tasks, viewing tasks, saving, and loading.
Example Workflow:
The user selects Add Task.
Enters task details: title, description, and due date.
Task is saved to the task_list.
The user selects View Tasks.
Displays all tasks with options to filter by status.
The user selects Mark Task Completed.
Marks a specific task as completed.
The user selects Save Tasks.
Saves the task_list to a file.
The user selects Load Tasks.
Loads previously saved tasks from the file.
