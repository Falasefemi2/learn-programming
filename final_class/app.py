import sys
import os
import json

def display_tasks(tasks):
    """Displays the list of tasks with numbering."""
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

def save_tasks(file_name, tasks):
    """Saves the tasks list to the JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file)

def load_tasks(file_name):
    """Loads tasks from the JSON file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

# Step 1: Check for command-line arguments
if len(sys.argv) != 2:
    print("Usage: python app.py <file_name>")
    sys.exit(1)

file_name = sys.argv[1]

# Step 2: Check if the file exists or create it
if not os.path.exists(file_name):
    print(f"{file_name} does not exist. Creating it...")
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump([], file)  # Save an empty list to the file
    print(f"{file_name} created successfully")
else:
    print(f"{file_name} already exists.")

# Load tasks from the file
tasks = load_tasks(file_name)

# Step 3: Show a menu for user interaction
while True:
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # View tasks
        print("\nYour Tasks:")
        display_tasks(tasks)

    elif choice == "2":
        # Add a new task
        new_task = input("Enter the new task: ")
        tasks.append(new_task)
        save_tasks(file_name, tasks)
        print(f"Task '{new_task}' added successfully!")

    elif choice == "3":
        # Update a task
        print("\nYour Tasks:")
        display_tasks(tasks)
        if tasks:
            try:
                task_num = int(input("Enter the task number to update: "))
                if 1 <= task_num <= len(tasks):
                    updated_task = input("Enter the updated task: ")
                    tasks[task_num - 1] = updated_task
                    save_tasks(file_name, tasks)
                    print(f"Task {task_num} updated successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        # Delete a task
        print("\nYour Tasks:")
        display_tasks(tasks)
        if tasks:
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    save_tasks(file_name, tasks)
                    print(f"Task '{deleted_task}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        # Exit
        print("Exiting Task Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")