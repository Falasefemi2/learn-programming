import os
import re
import json

def display_contacts(contacts):
    """Display contacts"""
    if contacts:
        for i,contact in enumerate(contacts,start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found!!!")
        
def validate_phone_number(phone):
    """Validate phone number to ensure it starts with +234 and is followed by 10 digits."""
    pattern = r"^\+234\d{10}$"
    return bool(re.match(pattern, phone))

def validate_email(email):
    """Validate email address for proper format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

        
def add_contacts(contacts):
    """Add new contacts"""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter the email: ").strip()

    # Validate the inputs
    if not validate_phone_number(phone):
        print("Invalid phone number. It should start with +234 and have 10 digits after.")
        return  # Exit without adding the contact

    if not validate_email(email):
        print("Invalid email format.")
        return  # Exit without adding the contact

    # Check for duplicate phone numbers
    if any(contact['phone'] == phone for contact in contacts):
        print("A contact with this phone number already exists!")
        return  # Exit without adding the contact

    # Add contact if all validations pass
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")




    
def save_contacts(file_name, contacts):
    """Save contact to file"""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(contacts, file)
        
def load_contacts(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist
    except json.JSONDecodeError:
        return []  # Return an empty list if the file is invalid
    
def search_contacts(contacts):
    """Search for contact"""
    if not contacts:
        print("No contact found!!")
        return
    
    # Search menu
    print("\nSearch Contacts:")
    print("1. Search by Name")
    print("2. Search by Phone")
    print("3. Search by Email")
    print("4. Cancel Search")
    
    # Get search choice
    search_choice = input("Enter your search option: ").strip()
    
    # Validate choice
    if search_choice not in ["1", "2", "3", "4"]:
        print("Invalid search option!")
        return
    
    # Get search term
    search_term = input("Enter search term: ").strip().lower()
    
    # if search term is empty
    if not search_term:
        print("Search cannot be empty!")
        return
    
    # Perform search based on selected option
    results = []
    if search_choice == "1":
        # Search by name (partial, case-sensitive)
        results = [
            contact for contact in contacts
            if search_term in contact['name'].lower()
        ]
    elif search_choice == "2":
        # Search by phone (partial, case-insensitive)
        results = [
            contact for contact in contacts 
            if search_term in contact['phone'].lower()
        ]
    elif search_choice == "3":
        # Search by email (partial, case-insensitive)
        results = [
            contact for contact in contacts 
            if search_term in contact['email'].lower()
        ]

    # Display results
    if results:
        print("\nSearch Results:")
        display_contacts(results)
        print(f"\nFound {len(results)} matching contact(s)")
    else:
        print("No contacts found matching the search term.")
        
def update_contacts(contacts):
    """Update contact"""
    if not contacts:
        print("No contacts found!!")
        return
    
    # Search for contact to update
    print("\nFind contact to update:")
    search_term = input("Enter name or phone number to find contact: ").strip().lower()

    # Find matching contacts
    matching_contacts = [
        contact for contact in contacts 
        if search_term in contact['name'].lower() or 
           search_term in contact['phone'].lower()
    ]
    
    # Handle search results
    if not matching_contacts:
        print("No matching contacts found!")
        return
    
    # Displaying matching contacts if multiple found
    if len(matching_contacts) > 1:
        print("\nMultiple contacts found:")
        display_contacts(matching_contacts)
        
        # Let user choose which contact to update
        while True:
            try:
                index = int(input("Enter the number of the contact to update: ")) - 1
                contact_to_update = matching_contacts[index]
                break
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
    else:
        contact_to_update = matching_contacts[0]
        
        # Update menu
    while True:
        print("\nUpdate Menu:")
        print("1. Update Name")
        print("2. Update Phone")
        print("3. Update Email")
        print("4. Cancel Update")

        update_choice = input("Enter your choice: ").strip()

        if update_choice == "4":
            print("Update cancelled.")
            return

        # Get new value
        if update_choice == "1":
            new_name = input("Enter new name: ").strip()
            contact_to_update['name'] = new_name
        elif update_choice == "2":
            while True:
                new_phone = input("Enter new phone number: ").strip()
                
                # Check for duplicate phone number
                if any(contact['phone'] == new_phone and contact != contact_to_update for contact in contacts):
                    print("This phone number is already in use by another contact!")
                    continue
                
                contact_to_update['phone'] = new_phone
                break
        elif update_choice == "3":
            new_email = input("Enter new email: ").strip()
            contact_to_update['email'] = new_email
        else:
            print("Invalid choice. Please try again.")
            continue

        print("Contact updated successfully!")
        break
    
def delete_contacts(contacts):
    """Delete existing contact"""
    # Check if contacts exist
    if not contacts:
        print("No contacts to delete!")
        return

    # Search for contact to delete
    print("\nFind contact to delete:")
    search_term = input("Enter name or phone number to find contact: ").strip().lower()

    # Find matching contacts
    matching_contacts = [
        contact for contact in contacts 
        if search_term in contact['name'].lower() or 
           search_term in contact['phone'].lower()
    ]

    # Handle search results
    if not matching_contacts:
        print("No matching contacts found!")
        return

    # Display matching contacts if multiple found
    if len(matching_contacts) > 1:
        print("\nMultiple contacts found:")
        display_contacts(matching_contacts)
        
        # Let user choose which contact to delete
        while True:
            try:
                index = int(input("Enter the number of the contact to delete: ")) - 1
                contact_to_delete = matching_contacts[index]
                break
            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
    else:
        contact_to_delete = matching_contacts[0]

    # Confirmation before deletion
    print("\nContact to be deleted:")
    print(f"Name: {contact_to_delete['name']}")
    print(f"Phone: {contact_to_delete['phone']}")
    print(f"Email: {contact_to_delete['email']}")

    # Deletion confirmation
    confirm = input("Are you sure you want to delete this contact? (yes/no): ").strip().lower()
    
    if confirm in ['yes', 'y']:
        # Remove the contact
        contacts.remove(contact_to_delete)
        print("Contact deleted successfully!")
    else:
        print("Deletion cancelled.")



# Main Program
file_name = "contact.json"
contacts = load_contacts(file_name)

while True:
    print("\nContact Book..")
    print("1. View Contact")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_contacts(contacts)
    elif choice == "2":
        add_contacts(contacts)
        save_contacts(file_name, contacts)
    elif choice == "3":
        search_contacts(contacts)
    elif choice == "4":
        update_contacts(contacts)
        save_contacts(file_name, contacts)
    elif choice == "5":
        delete_contacts(contacts)
        save_contacts(file_name, contacts)
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

        