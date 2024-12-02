"""Module providing a function printing python version."""
import json
import re

class ContactManager:
    """Class fro contact manager
    """
    def __init__(self, file_name):
        self.file_name = file_name
        self.contacts = self.load_contacts()

        
    def load_contacts(self):
        """Load contacts from a file."""
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

        
    def save_contacts(self):
        """Save contact to file"""
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.contacts, file)
            
    def display_contacts(self):
        """Display all contacts"""
        if self.contacts:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No contact found!")
            

class ContactBook(ContactManager):
    """_summary_

    Args:
        ContactManager (_type_): _description_
    """
    def __init__(self, file_name):
        super().__init__(file_name)
    
    def validate_phone_number(self, phone):
        """Validate phone number to ensure it starts with +234 and has 10 digits."""
        pattern = r"^\+234\d{10}$"
        return bool(re.match(pattern, phone))
    
    def validate_email(self, email):
        """Validate email address."""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))
    
    def add_contact(self):
        """Add a new contact
        """
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact phone: ").strip()
        email = input("Enter the email: ").strip()
        
        if not self.validate_phone_number(phone):
            print("Invalid phone number. It should start with +234 and have 10 digits")
            return
        
        if not self.validate_email(email):
            print("Invalid email format")
            return
        
        if any(contact['phone'] == phone for  contact in self.contacts):
            print("A contact  with this phone number already exists!!")
            return
        
        self.contacts.append({"name": name, "phone": phone, "email": email})
        print("Contact added successfully!")
        self.save_contacts()
        
    def search_contact(self):
        """Search for contact
        """
        if not self.contacts:
            print("No contact found!")
            return
        
        search_term = input("Enter name, phone, or email to search: ").strip().lower()
        results = [
            contact for contact in self.contacts
            if search_term in contact['name'].lower() or search_term in contact['phone'] or search_term in contact['email'].lower()
        ]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No matching contacts found!!")
            
    def update_contact(self):
        """Update an existing contact."""
        if not self.contacts:
            print("No contacts found!")
            return

        search_term = input("Enter name or phone of contact to update: ").strip().lower()
        matching_contacts = [
            contact for contact in self.contacts
            if search_term in contact['name'].lower() or search_term in contact['phone']
        ]

        if not matching_contacts:
            print("No matching contacts found!")
            return

        if len(matching_contacts) > 1:
            print("Multiple contacts found:")
            for i, contact in enumerate(matching_contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            index = int(input("Enter the number of the contact to update: ")) - 1
            contact_to_update = matching_contacts[index]
        else:
            contact_to_update = matching_contacts[0]

        print("Updating contact...")
        contact_to_update['name'] = input(f"Enter new name ({contact_to_update['name']}): ").strip() or contact_to_update['name']
        contact_to_update['phone'] = input(f"Enter new phone ({contact_to_update['phone']}): ").strip() or contact_to_update['phone']
        contact_to_update['email'] = input(f"Enter new email ({contact_to_update['email']}): ").strip() or contact_to_update['email']
        print("Contact updated successfully!")
        self.save_contacts()
        
    def delete_contact(self):
        """Delete a contact"""
        if not self.contacts:
            print("No contact found!")
            return
        
        search_term = input("Enter name or phone of contact to delete: ").strip().lower()
        matching_contacts = [
            contact for contact in self.contacts
            if search_term in contact['name'].lower() or search_term in contact['phone']
        ]

        if not matching_contacts:
            print("No matching contacts found!")
            return

        if len(matching_contacts) > 1:
            print("Multiple contacts found:")
            for i, contact in enumerate(matching_contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            index = int(input("Enter the number of the contact to delete: ")) - 1
            contact_to_delete = matching_contacts[index]
        else:
            contact_to_delete = matching_contacts[0]

        self.contacts.remove(contact_to_delete)
        print("Contact deleted successfully!")
        self.save_contacts()
        
# Main Program
if __name__ == "__main__":
    contact_book = ContactBook("contacts.json")
    
    while True:        
        print("\nContact Book Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            contact_book.display_contacts()
        elif choice == "2":
            contact_book.add_contact()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            print("Goodbye!!")
            break
        else:
            print("Invalid choice. Please try again!!")






            
    