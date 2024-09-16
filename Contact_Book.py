contacts = []
def add_contact(name, phone, email, address):
    contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(query):
    found_contacts = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
    if not found_contacts:
        print("No contacts found.")
        return
    for contact in found_contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def update_contact(name, new_phone=None, new_email=None, new_address=None):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact(name):
    global contacts
    contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    print("Contact deleted successfully.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            add_contact(name, phone, email, address)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_contact(query)
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            new_phone = input("Enter new phone number (or press Enter to skip): ")
            new_email = input("Enter new email (or press Enter to skip): ")
            new_address = input("Enter new address (or press Enter to skip): ")
            update_contact(name, new_phone, new_email, new_address)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            delete_contact(name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
