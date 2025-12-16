# CONTACT BOOK APPLICATION

contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n--- Contact List ---")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()

def search_contact():
    key = input("Enter name or phone to search: ")
    found = False
    for c in contacts:
        if key.lower() in c['name'].lower() or key in c['phone']:
            print("\nContact Found:")
            print(c)
            found = True
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter name of contact to update: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input("New Phone: ")
            c['email'] = input("New Email: ")
            c['address'] = input("New Address: ")
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter name of contact to delete: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("---- CONTACT BOOK ----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you for using Contact Book!")
            break
        else:
            print("Invalid choice!\n")

menu()
