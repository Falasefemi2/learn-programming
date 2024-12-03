import json
import re

class ContactManager:
    def __init__(self, fileName):
        self.fileName = fileName
        self.contacts = self.loadContacts()
    
    def loadContacts(self):
        try:
            with open(self.fileName, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def saveContacts(self):
        with open(self.fileName, "w", encoding="utf-8") as file:
            json.dump(self.contacts, file)
            
    def displayContacts(self):
        if self.contacts:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No contact found!!")
            
class ContactBook(ContactManager):
    def __init__(self, fileName):
        super().__init__(fileName)
        
    def validateEmail(self, email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))
    
    def addContact(self):
        name = input("Enter contact name: ").strip()
        phone = input("Enter contact phone: ").strip()
        email = input("Enter contact email: ").strip()
        
        if not self.validateEmail(email):
            print("Invalid email format")
            return
        
        self.contacts.append({"name": name, "email": email, "phone": phone})
        print("Contact added successfully!!")
        self.saveContacts()
        
    def searchContact(self):
        if not self.contacts:
            print("No contact found!!")
            return
        
        searchTerm = input("Enter name or phone of contact to update: ").strip().lower()
        result = [
            contact for contact in self.contacts
            if searchTerm in contact['name'].lower() or searchTerm  in contact['email'].lower()
        ]
        if result:
            print("\nSearch Result:")
            for contact in result:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        else:
            print("No matching contacts found!!")
            
    def updateContact(self):
        if not self.contacts:
            print("No contact found!")
            return
        searchTerm = input("Enter name or phone of contact you want to update: ").strip().lower()
        matchingContacts = [
            contact for contact in self.contacts
            if searchTerm in contact['name'].lower() or searchTerm in contact['phone']
        ]
        if not matchingContacts:
            print("No matching contacts found!!")
            return
        if len(matchingContacts) > 1:
            print("Multiple contacts found")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            index = int(input("Enter the index number of the contact to update: ")) - 1
            contactToUpdate = matchingContacts[index]
        else:
            contactToUpdate = matchingContacts[0]
            
        print("Updating contact...")
        contactToUpdate['name'] = input(f"Enter new name ({contactToUpdate['name']}): ").strip() or contactToUpdate['name']
        contactToUpdate['phone'] = input(f"Enter new phone ({contactToUpdate['phone']}): ").strip() or contactToUpdate['phone']
        contactToUpdate['email'] = input(f"Enter new email ({contactToUpdate['email']}): ").strip() or contactToUpdate['email']
        print("Contact updated successfully1!")
        self.saveContacts()
        
    def deleteContact(self):
        if not self.contacts:
            print("No contact found!!")
            return
        searchTerm = input("Enter name or phone of contact to delete: ").strip().lower()
        matchingContact = [
            contact for contact in self.contacts
            if searchTerm in contact['name'].lower() or searchTerm in contact['phone']
        ]
        
        if not matchingContact:
            print("No matching contacts found!!")
            return
        
        if len(matchingContact) > 1:
            print("Multiple contacts found.")
            for i,contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                index = int(input("Enter the number of the contact to delete: ")) - 1
                contactToDelete = matchingContact[index]
        else:
            contactToDelete = matchingContact[0]
            
        self.contacts.remove(contactToDelete)
        print("Contact deleted successfully!!")
        self.saveContacts()
        
if __name__ == "__main__":
    contactBook = ContactBook("contact.json")
    
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
            contactBook.displayContacts()
        elif choice == "2":
            contactBook.addContact()
        elif choice == "3":
            contactBook.searchContact()
        elif choice == "4":
            contactBook.updateContact()
        elif choice == "5":
            contactBook.deleteContact()
        elif choice == "6":
            print("Nice, Goodbye!!")
            break
        else:
            print("Invalid choice. Please try again!!")