"""
📒 Mini-Proyecto: Agenda de Contactos
📝 Descripción
Crea una pequeña agenda en donde se guardara el nombre, el celular, estado civil, genero, todo esto se guardara dentro de un 
lista para que tengamos una lista de contactos

Agregar un nuevo contacto.
Buscar un contacto por su nombre o celular.
Mostrar todos los contactos.
Modificar un contacto en especifico
Eliminar un contacto.
📦 Requisitos
Usar un diccionario para guardar la informacion y dentro de una lista guarda todos estos contactos
plus: a la hora de eliminar o modificar que me mustre los contactos existentes para asi verificar cual quiero modificar
"""


# Main list to store all contacts
contacts = []

# Validates that the phone contains only digits
def is_valid_phone(phone):
    return phone.isdigit()

# Validates that the gender input is acceptable
def is_valid_gender(gender):
    return gender.lower() in ["male", "female", "other"]

# Validates that the marital status input is acceptable
def is_valid_status(status):
    return status.lower() in ["single", "married", "other"]

# Show all contacts in the list
def show_contacts():
    if not contacts:
        print("📭 No contacts found.")  # If the list is empty
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Marital Status: {contact['marital_status']}, Gender: {contact['gender']}")

# Add a new contact with input validations
def add_contact():
    name = input("👤 Enter contact name: ").strip().title()

    phone = input("📞 Enter phone number: ").strip()
    if not is_valid_phone(phone):
        print("❌ Phone number must contain only digits.")
        return

    marital_status = input("💍 Enter marital status (Single/Married/Other): ").strip().title()
    if not is_valid_status(marital_status):
        print("❌ Marital status must be 'Single', 'Married', or 'Other'.")
        return

    gender = input("🚻 Enter gender (Male/Female/Other): ").strip().title()
    if not is_valid_gender(gender):
        print("❌ Gender must be 'Male', 'Female', or 'Other'.")
        return

    # Add the contact as a dictionary into the list
    contacts.append({
        "name": name,
        "phone": phone,
        "marital_status": marital_status,
        "gender": gender
    })
    print(f"✅ Contact '{name}' added successfully!")

# Search for a contact by name or phone number
def search_contact():
    keyword = input("🔍 Enter name or phone number to search: ").strip().lower()
    found = False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword == contact["phone"]:
            print(f"✅ Found: {contact}")
            found = True
    if not found:
        print("❌ Contact not found.")

# Update an existing contact’s information
def update_contact():
    show_contacts()
    if not contacts:
        return
    try:
        index = int(input("✏️ Enter the number of the contact to update: ")) - 1
        if index < 0 or index >= len(contacts):
            print("❌ Invalid contact number.")
            return
    except ValueError:
        print("❌ Invalid input. Must be a number.")
        return

    contact = contacts[index]

    print("🔁 Leave a field empty to keep the current value.")

    name = input(f"👤 New name (current: {contact['name']}): ").strip().title()
    phone = input(f"📞 New phone (current: {contact['phone']}): ").strip()
    marital_status = input(f"💍 New marital status (current: {contact['marital_status']}): ").strip().title()
    gender = input(f"🚻 New gender (current: {contact['gender']}): ").strip().title()

    # Validate only if input is provided
    if phone and not is_valid_phone(phone):
        print("❌ Phone number must contain only digits.")
        return

    if marital_status and not is_valid_status(marital_status):
        print("❌ Marital status must be 'Single', 'Married', or 'Other'.")
        return

    if gender and not is_valid_gender(gender):
        print("❌ Gender must be 'Male', 'Female', or 'Other'.")
        return

    # Update only the provided fields
    if name:
        contact["name"] = name
    if phone:
        contact["phone"] = phone
    if marital_status:
        contact["marital_status"] = marital_status
    if gender:
        contact["gender"] = gender

    print("✅ Contact updated successfully!")

# Delete a contact from the list
def delete_contact():
    show_contacts()
    if not contacts:
        return
    try:
        index = int(input("🗑️ Enter the number of the contact to delete: ")) - 1
        if index < 0 or index >= len(contacts):
            print("❌ Invalid contact number.")
            return
    except ValueError:
        print("❌ Invalid input. Must be a number.")
        return

    deleted = contacts.pop(index)
    print(f"✅ Contact '{deleted['name']}' deleted successfully.")

# Main interactive menu
def menu():
    while True:
        print("\n📒 Contact Agenda Menu")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Show All Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        # Handle user's choice
        match choice:
            case "1":
                add_contact()
            case "2":
                search_contact()
            case "3":
                show_contacts()
            case "4":
                update_contact()
            case "5":
                delete_contact()
            case "6":
                print("👋 Goodbye!")
                break
            case _:
                print("❌ Invalid option. Try again.")

# Run the program
menu()
