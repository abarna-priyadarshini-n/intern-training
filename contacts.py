contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print("Contact added successfully.")

def find_contact(name):
    try:
        print(f"{name} : {contacts[name]}")
    except KeyError:
        print("Contact not found.")

def list_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("\nContact List")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")