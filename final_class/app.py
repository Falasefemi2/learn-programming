"""Module providing a function printing python version."""

import sys
import os
import json

# Step 1: Check for command-line arguments
if len(sys.argv) != 2:
    print("Usage: Python app.py <file_name>")
    sys.exit(1)
    
# Get the file name from the arguments
file_name = sys.argv[1]

# Step 2: Check if the file exists or create it
if not os.path.exists(file_name):
    print(f"{file_name} does not exist. Creating it...")
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump([], file) # Save an empty list to the file
    print(f"{file_name} created successfully")
else:
    print(f"{file_name} already exists.")
    
# Step 3: Read and display the file content
try:
    with open(file_name, "r", encoding="utf-8") as file:
        tasks = json.load(file) # Load tasks from the file
        print(f"Loaded tasks: {tasks}")
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)
    
# Step 2: Show a menu for user interaction
while True:
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        # view task
        print("\nYour Tasks:")
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No task found.")
    elif choice == "2":
        # Add new task
        new_task = input("Enter the new task: ")
        tasks.append(new_task)
        
        # Save the updated task list to the file
        with open(file_name, "w") as file:
            json.dump(tasks, file)
        print(f"Task '{new_task}' added successfully!")
    elif choice == "3":
        # Update a task
        print("\nYour Tasks:")
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to update: "))
                if 1 <= task_num <= len(tasks):
                    updated_task = input("Enter the updated task: ")
                    tasks[task_num - 1] = updated_task
                    with open(file_name, "w") as file:
                        json.dump(tasks, file)
                    print(f"Task {task_num} updated successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks found to update.")
            
    elif choice == "4":
        # Delete a task
        print("\nYour Tasks:")
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    with open(file_name, "w") as file:
                        json.dump(tasks, file)
                    print(f"Task '{deleted_task}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks found to delete.")
            
    elif choice == "5":
        # Exit
        print("Exiting Task Manager. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 5")