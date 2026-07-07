import contacts
import todo

while True:
    print("\n===== FUNCTIONS EXERCISES =====")
    print("1. Contact Book")
    print("2. To-Do List")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # CONTACT BOOK
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
                contacts.add_contact(name, phone)

            elif contact_choice == "2":
                name = input("Enter name to search: ")
                contacts.find_contact(name)

            elif contact_choice == "3":
                contacts.list_contacts()

            elif contact_choice == "4":
                break

            else:
                print("Invalid choice!")

    # TO-DO LIST
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
                todo.add_task(task)

            elif task_choice == "2":
                task = input("Enter task to remove: ")
                todo.remove_task(task)

            elif task_choice == "3":
                todo.show_tasks()

            elif task_choice == "4":
                break

            else:
                print("Invalid choice!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")