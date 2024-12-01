import os
import json
import sys

def display_task(tasks):
    """Print all tasks."""
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

def save_task(file_name, tasks):
    """Save tasks to file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file)

def load_task(file_name):
    """Load tasks from file."""
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            tasks = json.load(f)
            if not isinstance(tasks, list):
                print("Invalid file format. Resetting tasks to an empty list.")
                return []
            return tasks
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def get_task_index(tasks, prompt):
    """Get a valid task index from the user."""
    try:
        task_num = int(input(prompt))
        if 1 <= task_num <= len(tasks):
            return task_num - 1
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    return None

if len(sys.argv) != 2:
    print("Usage: python main.py <file_name>")
    sys.exit(1)

file_name = sys.argv[1]

if not os.path.exists(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump([], file)
else:
    print(f"Loading tasks from {file_name}...")

tasks = load_task(file_name)

while True:
    print("\nTask Manager")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nYour Tasks:")
        display_task(tasks)

    elif choice == "2":
        new_task = input("Enter task you want to add: ").strip()
        if new_task:
            tasks.append(new_task)
            save_task(file_name, tasks)
            print("New Task added successfully")
        else:
            print("Task cannot be empty.")

    elif choice == "3":
        display_task(tasks)
        if tasks:
            index = get_task_index(tasks, "Enter the task number you want to update: ")
            if index is not None:
                updated_task = input("Enter the updated task: ").strip()
                if updated_task:
                    tasks[index] = updated_task
                    save_task(file_name, tasks)
                    print(f"Task updated successfully")
                else:
                    print("Task cannot be empty.")

    elif choice == "4":
        display_task(tasks)
        if tasks:
            index = get_task_index(tasks, "Enter the task number to delete: ")
            if index is not None:
                deleted_task = tasks.pop(index)
                save_task(file_name, tasks)
                print(f"Task '{deleted_task}' deleted successfully!")

    elif choice == "5":
        confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
        if confirm == 'y':
            print("Exiting Task Manager. Goodbye!")
            break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
