from datetime import datetime, date
import json
import os


class Tasks:
    def __init__(self, title, description, due_date, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __str__(self) -> str:
        return (
            f"Title: {self.title}, Description: {self.description}, "
            f"Due Date: {self.due_date}, Completed: {self.completed}"
        )


task_list = []


def task_input():
    while True:
        title = input("Enter task title: ")
        if title:
            break
        print("Title cannot be empty.")

    while True:
        description = input("Enter task description: ")
        if description:
            break
        print("Description cannot be empty.")

    while True:
        date_str = input("Enter due date (DD-MM-YYYY): ")
        try:
            due_date = datetime.strptime(date_str, "%d-%m-%Y").date()
            if due_date < date.today():
                print("Due date cannot be in the past.")
                continue
            break
        except ValueError:
            print("Invalid date format. Please enter in the format DD-MM-YYYY.")
    return title, description, due_date


def add_task():
    title, description, due_date = task_input()
    new_task = Tasks(title, description, due_date)
    task_list.append(new_task)
    print(f"Task added to task list: {new_task}")
    return new_task


def view_task():
    if not task_list:
        print("No task found.")
        return

    print("\n--- Task List ---")
    for index, task in enumerate(task_list, 1):
        print(f"{index}. {task}")


def mark_task_completed():
    if not task_list:
        print("No task found.")
        return

    view_task()
    try:
        index = int(input("Enter the index of the task to mark completed: ")) - 1
        if 0 <= index < len(task_list):
            task_list[index].mark_completed()
            print(f"Task marked completed: {task_list[index]}")
            save_task()  # Immediately save the updated task list
        else:
            print("Invalid index.")
    except ValueError:
        print("Enter a valid index.")




def get_incomplete_task():
    incomplete_tasks = [task for task in task_list if not task.completed]

    if not incomplete_tasks:
        print("No incomplete tasks found.")
        return incomplete_tasks

    print("\n--- Incomplete Tasks ---")
    for task in incomplete_tasks:
        print(task)

    return incomplete_tasks


def save_task():
    tasks_data = []
    for task in task_list:
        task_dict = {
            "title": task.title,
            "description": task.description,
            "due_date": task.due_date.strftime("%d-%m-%Y"),
            "completed": task.completed,
        }
        tasks_data.append(task_dict)

    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks_data, file, indent=4)
        print("Tasks saved successfully.")
    except IOError:
        print("Error saving tasks.")



def load_task():
    if not os.path.exists("tasks.json"):
        with open("tasks.json", "w") as file:
            json.dump([], file)
        print("No task data found. Created an empty task file.")
        return

    print("\n--- Loaded Task Data ---")
    try:
        with open("tasks.json", "r") as file:
            tasks_data = json.load(file)
            task_list.clear()  # Clear current task list to avoid duplicates
            for task_data in tasks_data:
                task = Tasks(
                    task_data["title"],
                    task_data["description"],
                    datetime.strptime(task_data["due_date"], "%d-%m-%Y").date(),
                    task_data["completed"],
                )
                task_list.append(task)
                print(task)
    except (IOError, ValueError):
        print("Error loading task data.")



def main():
    while True:
        print("\n--- Task Management System ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Get incomplete tasks")
        print("5. Save task data")
        print("6. Load task data")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            get_incomplete_task()
        elif choice == "5":
            save_task()
        elif choice == "6":
            load_task()
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
