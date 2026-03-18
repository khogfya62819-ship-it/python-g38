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

keys = ["name", "phone", "email", "address", "notes", "added_time"]

contact = dict.fromkeys(keys)

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

        display_menu()

        choice = input(f"Enter your choice (1-{len(menu_items)}): ").strip()

        match choice:
            case '1':
                add_contact()
            case '2':
                view_contacts()
            case '3':
                search_contact()
            case '4':
                edit_contact()
            case '5':
                delete_contact()
            case '6':
                print("👋 Thank you for using the Phone Book CLI. Goodbye!")
                break
            case _:
                print("❌ Invalid choice. Please enter a number between 1 and 6.")
            

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

# def add_contact():
#     """Add a new contact."""
    
#     name = get_field("name")
#     phone = get_field("phone number")
#     email = get_field("email")
#     address = get_optional_field("address") 
#     notes = get_optional_field("notes")
#     added_time = datetime.now().strftime("%Y-%m-%d")


#     if name and phone:
#         contacts.append([name, phone, email, address, notes, added_time])
#         print(f"Contact '{name}' added successfully.")
#     else:
#         print("❌ Name and phone number cannot be empty.")

def add_contact():
    """Add a new contact."""
    
    for key in keys:
        if key in ["name", "phone", "email"]:
            contact[key] = get_field(key)
        elif key == "added_time":
            contact[key] = datetime.now().strftime("%Y-%m-%d")
        else:
            contact[key] = get_optional_field(key)
    
    contacts.append(contact.copy())
    print(f"✅ Contact '{contact['name']}' added successfully!")

# def data_table(contacts, title):

#     print("\n" + "="*80)
#     print(f"📱 {title.upper()}")
#     print("="*80)
#     print(f"{'No.':<3} {'Name':<20} {'Phone Number':<15} {'Email':<20} {'Added':<10}")
#     print("-"*80)

#     for idx, contact in enumerate(contacts, start=1):
#         name = contact[0]
#         phone = contact[1]
#         email = contact[2] if contact [2] else ""
#         added_time = contact[5]
#         print(f"{idx:<3} {name:<20} {phone:<15} {email:<20} {added_time:<10}")
#         print("="*80)

def data_table(contacts, title):

    print("\n" + "="*80)
    print(f"📱 {title.upper()}")
    print("="*80)
    print(f"{'No.':<3} {'Name':<20} {'Phone':<15} {'Email':<20} {'Added Time':<10}")
    print("-"*80)

    #
    results = []
    for idx, contact in enumerate(contacts, 1):
        for key in keys:
            if key in ["name", "phone", "email", "added_time"]:
                results.append(contact[key])

        print(f"{idx:<3} {results[0]:<20} {results[1]:<15} {results[2]:<20} {results[3]}")
        results.clear()
        print("="*80)

def view_contacts():
    """View all contacts."""
    if not contacts:
        print("📭 No contacts found.")
        return
    data_table(contacts, "Contact List")


# def search_contact(search_term):
#     """Search for a contact by name, phone number, or email."""
#     results = []
#     search_term = search_term.lower()

#     for contact in contacts:
#         # Safe access with check for None
#         c_name = contact[0].lower()
#         c_phone = contact[1].lower()
#         c_email = contact[2].lower() if contact[2] else ""
#         if (search_term in c_name or 
#                 search_term in c_phone or 
#                 search_term in c_email):
#             results.append(contact)

#     if not results:
#         print("🔍 No contacts found matching that search term.")        
#         return
    
#     data_table(results, "SEARCH RESULTS")

def search_contact():
    """Search for a contact by name, phone, or email."""
    
    search_results = []
    search_term = input("Enter name, phone number, or email to search: ").strip()
    search_term = normalize(search_term)

    for contact in contacts:
        for key in contact.keys():
            if key in ["name", "phone", "email"]:
                if search_term in contact[key].lower():
                    search_results.append(contact)
                    break

    if not search_results:
        print("🔍 No contacts found matching that search term.")
        return
    
    data_table(search_results, 'SEARCH RESULTS')

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
    contact['name'] = get_update_field("Name", contact['name'])
    contact['phone'] = get_update_field("Phone Number", contact['phone'])
    contact['email'] = get_update_field("Email", contact['email'])
    contact['address'] = get_update_field("Address", contact['address'], optional=True)
    contact['notes'] = get_update_field("Notes", contact['notes'], optional=True)
    contact['added_time'] = datetime.now().strftime("%Y-%m-%d")

    print(f"✅ Contact '{contact['name']}' updated successfully.")


def delete_contact():
    """Delete a contact."""
    if not contacts:
        print("📭 No contacts found.")
        return
    contact_id_str = input("Enter the contact ID to delete: ").strip()
    try:
        contact_id = int(contact_id_str)
        if contact_id < 1 or contact_id > len(contacts):
            print("❌ Invalid contact ID.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return
    
    confirm = input(f"Are you sure you want to delete contact '{contact_id}'? (y/n): ").strip().lower()
    if confirm == 'y':
        # del contacts[int(contact_id) - 1]
        # print(f"🗑 Contact '{contact_id}' deleted successfully.")
        deleted_contact = contacts.pop(contact_id - 1)
        print(f"🗑 Contact '{deleted_contact['name']}' deleted successfully.")
    else:
        print("Deletion cancelled.")

    # deleted_contact = contacts.pop(contact_id - 1)


main()
