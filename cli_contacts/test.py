
from datetime import datetime

contacts = []
keys = ["name", "phone", "email", "address", "notes", "added_time"]

contact = dict.fromkeys(keys)
# print(contact)
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
    
    for key in keys:
        if key in ["name", "phone", "email"]:
            contact[key] = get_field(key)
        elif key == "added_time":
            contact[key] = datetime.now().strftime("%Y-%m-%d")
        else:
            contact[key] = get_optional_field(key)
    # if contact ["name"] and contact["phone"]:
        contacts.append(contact.copy())
        print(f"✅ Contact '{contact['name']}' added successfully!")
    # else:
    #     print("❌ Name and phone number cannot be empty. Contact not added.")

def data_table(contacts, title):

    print("\n" + "="*50)
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
    data_table(contacts, "All Contacts")

def search_contact():
    """Search for a contact by name, phone, or email."""
    
    search_results = []
    search_term = input("Enter name, phone number, or email to search: ").strip
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

add_contact()
view_contacts()
search_contact()
# print(contacts)
