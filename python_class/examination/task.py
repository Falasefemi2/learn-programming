from datetime import datetime, date



class Tasks:
    def __init__(self, title, description, due_date, completed=False) :
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed
        
    def mark_completed(self):
        self.completed = True
        
    def __str__(self) -> str:
        return f"Title: {self.title}, Description: {self.description}, Due Date: {self.due_date}, Completed: {self.completed}"
    
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
            due_date= datetime.strptime(date_str, "%d-%m-%Y").date()
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
    return new_task

def view_task():
    pass

def get_incomplete_task():
    pass

def save_task():
    pass

def load_task():
    pass