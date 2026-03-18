from datetime import datetime

contacts = []

menu_items = (
    "Add Contact",
    "View All Contacts",
    "Search Contact",
    "Edit Contact",
    "Delete Contact",
    "Exit"
)

def display_menu():
    """Display the main menu."""

    print("\n=== Contact Manager Menu ===")
    for idx, item in enumerate(menu_items, start=1):
        print(f"{idx}. {item}")

def main():
    """Main contact manager loop."""

    while True:
        print("\n" + "="*60)
        print("📱 Simple Contact Manager")
        print("="*60)

        # print("=== Simple Contact Manager ===\n")

        display_menu()

        choice = input(f"Enter your choice (1-{len(menu_items)}): ").strip()

        match choice:
            case '1':
                # print("You chose to add a contact.")
                add_contact()
            case '2':
                # print("You chose to view all contacts.")
                view_contacts()
            case '3':
                # print("You chose to search for a contact.")
                search_term = input("Enter name, phone number, or email to search: ").strip()
                search_contact(search_term)
            case '4':
                # print("You chose to edit a contact.")
                edit_contact()
            case '5':
                # print("You chose to delete a contact.")
                id_str = input("Enter the contact number to delete: ").strip()
                delete_contact(id_str)
            case '6':
                # print("Exiting Contact Manager. Goodbye!")
                print("👋 Thank you for using the Phone Book CLI. Goodbye!")
                break
            case _:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")
            

    # while True:
    #     name = input("Enter contact name (or 'exit' to quit): ").strip()
    #     if name.lower() == 'exit':
    #         print("Exiting Contact Manager. Goodbye!")
    #         break
    #     if not name:
    #         print("Name cannot be empty. Please try again.")
    #         continue
    #     phone = input("Enter contact phone number: ").strip()
    #     if not phone:
    #         print("Phone number cannot be empty. Please try again.")
    #         continue
    #     contacts[name] = phone
    #     print(f"Contact '{name}' added with phone number '{phone}'.\n")
    # print("Your contacts:")
    # for name, phone in contacts.items():
    #     print(f"{name}: {phone}")
    # print("Thank you for using the Contact Manager!")

# added_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# added_time = datetime.now().strftime("%Y-%m-%d")
# print(f"Contact added at: {added_time}")

def normalize(name: str):
    return name.strip().lower()

def get_field(field):
    """Gets non-empty field from user."""
    while True:
        result = input(f"Enter {field}: ")
        if result:
            return normalize(result)
        print(f"❌ {field.title()} cannot be empty. Please try again.")

def get_optional_field(field):
    """Gets optional field from user."""
    result = input(f"Enter {field} (optional): ")
    return normalize(result) or None

def get_update_field(field, current, optional=False):
    """Gets field for updating an existing contact."""
    prompt = f"{field} [{current}]: "
    value = input(prompt).strip()
    if not value:
        return current
    if optional:
        return value or None
    return value

def add_contact():
    """Add a new contact."""
    # name = input("Enter contact name: ").strip()
    # phone = input("Enter phone number: ").strip()
    # email = input("Enter email (optional): ").strip()
    # address = input("Enter address (optional): ").strip() or None
    # notes = input("Enter notes (optional): ").strip() or None
    # added_time = datetime.now().strftime("%Y-%m-%d")

    name = get_field("name")
    phone = get_field("phone number")
    email = get_field("email")
    address = get_optional_field("address") 
    notes = get_optional_field("notes")
    added_time = datetime.now().strftime("%Y-%m-%d")


    if name and phone:
        contacts.append([name, phone, email, address, notes, added_time])
        print(f"Contact '{name}' added successfully.")
    else:
        print("❌ Name and phone number cannot be empty.")

# def view_contacts():
#     """View all contacts."""
#     if contacts:
#         print("\n=== All Contacts ===")
#         for idx, (name, phone) in enumerate(contacts, start=1):
#             print(f"{idx}. {name}: {phone}")
#     else:
#         print("📭 No contacts found.")

# def view_contacts():
#     """View all contacts."""
#     if not contacts:
#         print("📭 No contacts found.")
#         return
    
#     print("\n" + "="*80)
#     print("📱 CONTACT LIST")
#     print("="*80)
#     print(f"{'No.':<3} {'Name':<20} {'Phone Number':<15} {'Email':<20} {'Added':<10}")
#     print("-"*80)
#     for idx, contact in enumerate(contacts, start=1):

        # Contact structure: [name, phone, email, address, notes, added_time]
        # name = contact[0]
        # phone = contact[1]
        # email = contact[2] if contact [2] else ""
        # added_time = contact[5]
        # print(f"{idx:<3} {name:<20} {phone:<15} {email:<20} {added_time:<10}")
        # print("="*80)

def data_table(contacts, title):

    print("\n" + "="*80)
    print(f"📱 {title.upper()}")
    print("="*80)
    print(f"{'No.':<3} {'Name':<20} {'Phone Number':<15} {'Email':<20} {'Added':<10}")
    print("-"*80)

    for idx, contact in enumerate(contacts, start=1):
        name = contact[0]
        phone = contact[1]
        email = contact[2] if contact [2] else ""
        added_time = contact[5]
        print(f"{idx:<3} {name:<20} {phone:<15} {email:<20} {added_time:<10}")
        print("="*80)

def view_contacts():
    """View all contacts."""
    if not contacts:
        print("📭 No contacts found.")
        return
    data_table(contacts, "Contact List")

# def search_contact():
#     """Search for a contact by name."""
#     query = input("Enter name to search: ").strip().lower()
#     results = [(name, phone) for name, phone in contacts if query in name.lower()]
#     if results:
#         print("\n=== Search Results ===")
#         for idx, (name, phone) in enumerate(results, start=1):
#             print(f"{idx}. {name}: {phone}")
#     else:
#         print("🔍 No contacts found matching that name.")

def search_contact(search_term):
    """Search for a contact by name, phone number, or email."""
    results = []
    search_term = search_term.lower()

    for contact in contacts:
        # Safe access with check for None
        c_name = contact[0].lower()
        c_phone = contact[1].lower()
        c_email = contact[2].lower() if contact[2] else ""
        if (search_term in c_name or 
                search_term in c_phone or 
                search_term in c_email):
            results.append(contact)

    if not results:
        print("🔍 No contacts found matching that search term.")        
        return
    
    data_table(results, "SEARCH RESULTS")
    # print("\n" + "="*80)
    # print("📱 SEARCH RESULTS")
    # print("="*80)
    # print(f"{'No.':<3} {'Name':<20} {'Phone Number':<15} {'Email':<20}")
    # print("-"*80)
    # for idx, contact in enumerate(results, start=1):
    #     email = contact[2] if contact[2] else ""
    #     print(f"{idx:<3} {contact[0]:<20} {contact[1]:<15} {email:<20}")
    #     print("="*80)

# def edit_contact():
#     """Edit an existing contact."""
#     name = input("Enter the name of the contact to edit: ").strip()
#     for idx, (contact_name, name, phone) in enumerate(contacts):
#         if contact_name.lower() == name.lower():
#             new_name = input(f"Enter new name [{contact_name}]: ").strip() or contact_name
#             new_phone = input(f"Enter new phone number [{phone}]: ").strip() or phone
#             contacts[idx] = [new_name or contact_name, new_phone or phone]
#             print(f"Contact '{contact_name}' updated successfully.")
#             return
#     print("❌ Contact not found.")

def edit_contact():
    """Edit an existing contact."""
    
    if not contacts:
        print("📭 No contacts found.")
        return
    
    try:
        contact_id = int(input("\nEnter the ID of the contact to edit: "))
        if contact_id < 1 or contact_id > len(contacts):
            print("❌ Invalid contact ID.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return


    # Index is ID - 1
    idx = contact_id - 1
    contact = contacts[idx]

    print("Leave blank to keep current.")
    contact[0] = get_update_field("Name", contact[0])
    contact[1] = get_update_field("Phone Number", contact[1])
    contact[2] = get_update_field("Email", contact[2])
    contact[3] = get_update_field("Address", contact[3], optional=True)
    contact[4] = get_update_field("Notes", contact[4], optional=True)
    contact[5] = datetime.now().strftime("%Y-%m-%d")

    print(f"✅ Contact '{contact[0]}' updated successfully.")


# def delete_contact():
#     """Delete a contact."""
#     name = input("Enter the name of the contact to delete: ").strip()
#     for idx, (contact_name, phone) in enumerate(contacts):
#         if contact_name.lower() == name.lower():
#             del contacts[idx]
#             print(f"Contact '{contact_name}' deleted successfully.")
#             return
#     print("❌ Contact not found.")

def delete_contact(contact_id_str):
    """Delete a contact."""
    if not contacts:
        print("📭 No contacts found.")
        return
    try:
        contact_id = int(contact_id_str)
        if contact_id < 1 or contact_id > len(contacts):
            print("❌ Invalid contact number.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return
    deleted_contact = contacts.pop(contact_id - 1)
    #save_contacts_to_disk()
    print(f"🗑 Contact '{deleted_contact[0]}' deleted successfully.")

main()
