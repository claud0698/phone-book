import json
import os

def load_contacts(data_file):
    if os.path.exists(data_file):
        with open(data_file, "r", encoding="utf-8") as f:
            try:
                contacts = json.load(f)
                print(f"Loaded {len(contacts)} contacts from {data_file}.")
                return contacts
            except json.JSONDecodeError:
                print(f"Warning: {data_file} is corrupted or empty. Starting with an empty phonebook.")
    else:
        print("No contacts file found. Starting with an empty phonebook.")
    return []

def save_contacts(phonebook, data_file):
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump(phonebook, f, indent=2, ensure_ascii=False)

def get_input(prompt):
    value = input(prompt)
    if value.strip().lower() == 'exit':
        print("Goodbye!")
        exit(0)
    return value

def add_entry(phonebook, data_file):
    name = get_input("Enter name: ")
    address = get_input("Enter address: ")
    phone = get_input("Enter phone number: ")
    phonebook.append({"name": name, "address": address, "phone": phone})
    save_contacts(phonebook, data_file)
    print("Entry added.")

def view_entries(phonebook):
    if not phonebook:
        print("No entries found.")
        return
    for idx, entry in enumerate(phonebook, 1):
        print(f"{idx}. Name: {entry['name']}, Address: {entry['address']}, Phone: {entry['phone']}")

def edit_entry(phonebook, data_file):
    view_entries(phonebook)
    if not phonebook:
        return
    try:
        idx = int(get_input("Enter entry number to edit: ")) - 1
        if 0 <= idx < len(phonebook):
            name = get_input(f"Enter new name [{phonebook[idx]['name']}]: ") or phonebook[idx]['name']
            address = get_input(f"Enter new address [{phonebook[idx]['address']}]: ") or phonebook[idx]['address']
            phone = get_input(f"Enter new phone [{phonebook[idx]['phone']}]: ") or phonebook[idx]['phone']
            phonebook[idx] = {"name": name, "address": address, "phone": phone}
            save_contacts(phonebook, data_file)
            print("Entry updated.")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input.")

def delete_entry(phonebook, data_file):
    view_entries(phonebook)
    if not phonebook:
        return
    try:
        idx = int(get_input("Enter entry number to delete: ")) - 1
        if 0 <= idx < len(phonebook):
            del phonebook[idx]
            save_contacts(phonebook, data_file)
            print("Entry deleted.")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input.")

def main():
    DATA_FILE = "contacts.json"
    phonebook = load_contacts(DATA_FILE)
    # Show contacts immediately on startup
    print("\n--- Contact Book ---")
    view_entries(phonebook)
    while True:
        print("\nPhone Book Menu:")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Edit Entry")
        print("4. Delete Entry")
        print("5. Exit")
        choice = get_input("Choose an option: ")
        if choice == '1':
            add_entry(phonebook, DATA_FILE)
        elif choice == '2':
            view_entries(phonebook)
        elif choice == '3':
            edit_entry(phonebook, DATA_FILE)
        elif choice == '4':
            delete_entry(phonebook, DATA_FILE)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
