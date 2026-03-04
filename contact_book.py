# Contact Book Project using File Handling

file_name = "contacts.txt"


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    with open(file_name, "a") as f:
        f.write(name + "," + phone + "\n")

    print("Contact saved successfully")


def view_contacts():
    try:
        with open(file_name, "r") as f:
            contacts = f.readlines()

        if len(contacts) == 0:
            print("No contacts available")
            return

        print("\n---- Contact List ----")
        for contact in contacts:
            name, phone = contact.strip().split(",")
            print("Name:", name, "| Phone:", phone)

    except FileNotFoundError:
        print("No contact file found")


def search_contact():
    search_name = input("Enter name to search: ")

    found = False

    try:
        with open(file_name, "r") as f:
            for contact in f:
                name, phone = contact.strip().split(",")
                if name.lower() == search_name.lower():
                    print("Contact Found")
                    print("Name:", name)
                    print("Phone:", phone)
                    found = True

        if not found:
            print("Contact not found")

    except FileNotFoundError:
        print("File not found")


def delete_contact():
    delete_name = input("Enter name to delete: ")

    try:
        with open(file_name, "r") as f:
            contacts = f.readlines()

        with open(file_name, "w") as f:
            for contact in contacts:
                name, phone = contact.strip().split(",")

                if name.lower() != delete_name.lower():
                    f.write(contact)

        print("Contact deleted if it existed")

    except FileNotFoundError:
        print("File not found")


while True:

    print("\n====== CONTACT BOOK ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid choice")