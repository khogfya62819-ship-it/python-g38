
from datetime import datetime

contacts = {}

keys = ["name", "phone", "email", "address", "notes", "added_time"]
menu_items = (
    "Add Contact",
    "View All Contacts",
    "Search Contact",
    "Edit Contacts",
    "Delete Contact",
    "Exit"
)

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
    
    new_contact = {}  # Local dict!
    for key in keys:
        if key in ["name", "phone", "email"]:
            new_contact[key] = get_field(key)
        elif key == "added_time":
            new_contact[key] = datetime.now().strftime("%Y-%m-%d")
        else:
            new_contact[key] = get_optional_field(key)

    if new_contact["name"] and new_contact["phone"]:
        contacts[len(contacts) + 1] = new_contact
        print(f"✅ Contact '{new_contact['name']} added successfully")


def data_table(contacts_dict, title):

    print("\n" + "="*80)
    print(f"📱 {title.upper()}")
    print("="*80)
    print(f"{'No.':<3} {'Name':<20} {'Phone':<15} {'Email':<20} {'Added Time':<10}")
    print("-"*80)

    for idx, contact in enumerate(contacts_dict.values(), 1):
        print(f"{idx:<3} {contact['name']:<20} {contact['phone']:<15}"
              f"{contact['email']:<20} {contact['added_time'][:10]:<10}")
        
def view_contacts():
    """View all contacts."""
    if not contacts:
        print("📭 No contacts found.")
        return
    data_table(contacts, "Contact List")

def search_contact():
    """Search for a contact by name, phone, or email."""
    
    search_results = {}
    search_term = input("Enter name, phone number, or email to search: ").strip()
    search_term = normalize(search_term)

    for contact in contacts.values():
        for key in contact.keys():
            if key in ["name", "phone", "email"]:
                if search_term in contact[key].lower():
                    search_results[len(search_results)+1] = contact
                    break

    if not search_results:
        print("🔍 No contacts found matching that search term.")
        return
    
    data_table(search_results, 'SEARCH RESULTS')


# def search_contact():
#     """Search for a contact by name, phone, or email."""
#     search_term = normalize(input("Enter name, phone, or email to search: "))
#     search_results = {
#         id: contact for id, contact in contacts.items()
#         if any(search_term in normalize(contact[k]) for k in ["name", "phone", "email"])
#     }
#     if not search_results:
#         print("🔍 No contacts found matching your search.")
#         return
#     data_table(search_results, 'SEARCH RESULTS')


def display_menu():
    """Display the main menu."""

    print("\n=== Contact Manager Menu ===")
    for idx, item in enumerate(menu_items, start=1):
        print(f"{idx}. {item}")

    return input(f"Enter your choice (1-{len(menu_items)}): ").strip()

def edit_contact():
    """Edit an existing contact."""

    id_str = input("Enter the contact ID to edit: ").strip()
    if not id_str.isdigit() or int(id_str) not in contacts:
        print("❌ Invalid contact ID.")
        return
    
    contact_id = int(id_str)
    contact = contacts[contact_id]

    print(f"Editing contact '{contact['name']}' (ID: {contact_id})")

    for key in keys:
        if key in ["name", "phone", "email"]:
            contact[key] = get_update_field(key, contact[key])
        elif key == "added_time":
            contact[key] = datetime.now().strftime("%Y-%m-%d")
        else:
            contact[key] = get_update_field(key, contact[key], optional=True)

    print(f"✅ Contact '{contact['name']}' updated successfully.")
    
def delete_contact():
    """Delete a contact."""
    if not contacts:
        print("📭 No contacts found.")
        return
    
    view_contacts()
    id_str = input("\nEnter contact ID to delete: ").strip()

    if not id_str.isdigit() or int(id_str) not in contacts:
        print("❌ Invalid contact ID.")
        return
    
    name = contacts[int(id_str)]["name"]

    confirm = input(f"Are you sure you want to delete contact '{name}'? (y/n): ").strip().lower()
    if confirm == 'y':
        del contacts[int(id_str)]
        print(f"🗑 Contact '{name}' deleted successfully.")
    else:
        print("Deletion cancelled.")

def main():
    """Main contact manager loop."""

    while True:
        print("\n" + "="*60)
        print("📱 Simple Contact Manager")
        print("="*60)

        choice = display_menu()

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
            
main()
