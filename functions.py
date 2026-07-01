# CONTACT BOOK
contacts = {}
def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added successfully.")
def find_contact(name):
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found.")
def list_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("\nContact List")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

# TO-DO LIST
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

# MAIN MENU
while True:
    print("\n===== FUNCTIONS EXERCISES =====")
    print("1. Contact Book")
    print("2. To-Do List")
    print("3. Exit")
    choice = input("Enter your choice: ")

    # CONTACT BOOK
    # --------------------------
    if choice == "1":

        while True:

            print("\n--- Contact Book ---")
            print("1. Add Contact")
            print("2. Find Contact")
            print("3. List Contacts")
            print("4. Back to Main Menu")
            contact_choice = input("Enter your choice: ")
            if contact_choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                add_contact(name, phone)
            elif contact_choice == "2":
                name = input("Enter name to search: ")
                find_contact(name)
            elif contact_choice == "3":
                list_contacts()
            elif contact_choice == "4":
                break
            else:
                print("Invalid choice!")

    # TO-DO LIST
    # --------------------------
    elif choice == "2":

        while True:

            print("\n--- To-Do List ---")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Show Tasks")
            print("4. Back to Main Menu")
            task_choice = input("Enter your choice: ")
            if task_choice == "1":
                task = input("Enter task: ")
                add_task(task)
            elif task_choice == "2":
                task = input("Enter task to remove: ")
                remove_task(task)
            elif task_choice == "3":
                show_tasks()
            elif task_choice == "4":
                break
            else:
                print("Invalid choice!")
    elif choice == "3":
        break
    else:
        print("Invalid choice!")