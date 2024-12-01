import os
import json
import sys

# Display task
def display_task(tasks):
    """Function printing task."""
    if tasks:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.") 
        
# Save Task
def save_task(file_name, tasks):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(tasks, file)

        
# Load Task
def load_task(file_name):
    """Load tasks from file."""
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            tasks = json.load(f)
            if not isinstance(tasks, list):  # Ensure tasks is a list
                print("Invalid file format. Resetting tasks to an empty list.")
                return []
            return tasks
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    

if len(sys.argv) != 2:
    print("Usage: python main.py <file_name>")
    sys.exit(1)
    

file_name = sys.argv[1]

if not os.path.exists(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump([], file)  # Correctly saves an empty list
    print(f"{file_name} created successfully")
else:
    print(f"{file_name} already exists.")
    

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
        # View tasks
        print("\nYour Tasks:")
        display_task(tasks)
        
    elif choice == "2":
        # add task
        new_task = input("Enter task you want to add: ")
        tasks.append(new_task)
        save_task(file_name, tasks)
        print("New Task added successfully")
        
    elif choice == "3":
        display_task(tasks)
        if tasks:
            try:
                task_num = int(input("Enter the task number you want to update: "))
                if 1 <= task_num <= len(tasks):
                    updated_task = input("Enter the updated task: ")
                    tasks[task_num - 1] = updated_task
                    save_task(file_name, tasks)
                    print(f"Task {task_num} updated successfully")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
    elif choice == "4":
        display_task(tasks)
        if tasks:
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted_task = tasks.pop(task_num - 1)
                    save_task(file_name, tasks)
                    print(f"Task {deleted_task} deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number")
                
    elif choice == "5":
        # Exit
        print("Exiting Task Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")