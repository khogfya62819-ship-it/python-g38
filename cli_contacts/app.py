import ast
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
        contacts = load_contacts("data.txt")
        display_menu()
        choice = input(f"Enter your choice (1-{len(menu_items)}): ").strip()

        contacts = load_contacts("data.txt")

        match choice:
            case '1':
                add_contact(contacts)
            case '2':
                view_contacts(contacts)
            case '3':
                search_contact(contacts)
            case '4':
                edit_contact(contacts)
            case '5':
                delete_contact(contacts)
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

def add_contact(contacts):
    """Add a new contact."""
    
    for key in keys:
        if key in ["name", "phone", "email"]:
            contact[key] = get_field(key)
        elif key == "added_time":
            contact[key] = datetime.now().strftime("%Y-%m-%d")
        else:
            contact[key] = get_optional_field(key)
    
    contacts.append(contact.copy())
    save_contacts(contacts, "data.txt")
    print(f"✅ Contact '{contact['name']}' added successfully!")

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

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("📭 No contacts found.")
        return
    data_table(contacts, "Contact List")

def search_contact(contacts):
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

def edit_contact(contacts):
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


def delete_contact(contacts):
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

def save_contacts(contacts, db_name='data.txt'):
    with open(db_name, 'w') as f:
        for item in contacts:
            data_string = str(item)
            # f.write(data_string)
            f.write(data_string+'\n')

def load_contacts(db_name: str):
    """Load contacts from file."""
    try:
        results = []
        with open(db_name, 'r') as f:
            while f:
                line = f.readline()
                if line == "":
                    break
                item = ast.literal_eval(line)
                # item = str(line)
                results.append(item)
            return results
    except (FileNotFoundError, EOFError):
        return []

main()
