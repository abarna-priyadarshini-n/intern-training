tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully.")
    else:
        print("Task not found.")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nTo-Do List")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")