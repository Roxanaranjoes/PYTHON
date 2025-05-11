"""
Sistema de Gestión de Clientes de una Tienda
Descripción:
Crear un sistema para gestionar clientes de una tienda. Cada cliente tiene nombre, correo electrónico, teléfono y dirección de envío.

Requisitos:

Permitir agregar un nuevo cliente con nombre, correo electrónico, teléfono y dirección.

Permitir actualizar la dirección de un cliente.

Permitir eliminar un cliente.

Mostrar todos los clientes con su información.

Validar que el correo electrónico sea válido y el teléfono contenga solo números.

Posibles preguntas:

¿Cómo manejarías la actualización del teléfono de un cliente?

¿Cómo validarías que el correo electrónico sea correcto?

Ejemplo de pregunta:
"Imagina que estás creando un sistema de gestión de clientes para una tienda. Crea un programa donde puedas agregar, actualizar y eliminar clientes, y mostrar todos los clientes con su información. Asegúrate de que el correo electrónico sea válido y el teléfono contenga solo números."
"""
# Sistema de Gestión de Clientes

# Lista de clientes
customers = []

# Validación básica de email
def is_valid_email(email):
    return "@" in email and "." in email and email.index("@") < email.rindex(".")

# Agregar cliente
def add_customer():
    print("\n➕ Add New Customer")
    name = input("Enter customer name: ").strip().title()
    if not name:
        print("⚠️ Name cannot be empty.")
        return

    email = input("Enter email: ").strip()
    if not is_valid_email(email):
        print("⚠️ Invalid email format.")
        return

    phone = input("Enter phone number: ").strip()
    if not phone.isdigit():
        print("⚠️ Phone must contain only digits.")
        return

    home_address = input("Enter home address: ").strip()
    work_address = input("Enter work address: ").strip()

    customer = {
        "name": name,
        "email": email,
        "phone": phone,
        "addresses": {
            "home": home_address,
            "work": work_address
        }
    }

    customers.append(customer)
    print(f"✅ Customer '{name}' added successfully!")

# Actualizar direcciones
def update_address():
    print("\n✏️ Update Customer Address")
    if not customers:
        print("⚠️ No customers to update.")
        return

    name = input("Enter the name of the customer to update: ").strip().title()
    for customer in customers:
        if customer["name"] == name:
            home = input("Enter new home address: ").strip()
            work = input("Enter new work address: ").strip()
            customer["addresses"]["home"] = home
            customer["addresses"]["work"] = work
            print(f"✅ Addresses for '{name}' updated.")
            return

    print(f"❌ Customer '{name}' not found.")

# Eliminar cliente
def delete_customer():
    print("\n🗑️ Delete Customer")
    if not customers:
        print("⚠️ No customers to delete.")
        return

    name = input("Enter the name of the customer to delete: ").strip().title()
    for i, customer in enumerate(customers):
        if customer["name"] == name:
            customers.pop(i)
            print(f"✅ Customer '{name}' deleted.")
            return

    print(f"❌ Customer '{name}' not found.")

# Mostrar todos los clientes
def show_customers():
    print("\n📋 All Customers")
    if not customers:
        print("⚠️ No customers to show.")
        return

    for idx, customer in enumerate(customers, 1):
        print(f"{idx}. Name: {customer['name']}")
        print(f"   Email: {customer['email']}")
        print(f"   Phone: {customer['phone']}")
        print(f"   Home Address: {customer['addresses']['home']}")
        print(f"   Work Address: {customer['addresses']['work']}")

# Contar clientes usando lambda
def count_customers():
    count = (lambda lst: len(lst))(customers)
    print(f"\n🔢 Total number of customers: {count}")

# Menú principal
def main_menu():
    while True:
        print("\n====== CUSTOMER MANAGEMENT MENU ======")
        print("1. Add Customer")
        print("2. Update Address")
        print("3. Delete Customer")
        print("4. Show All Customers")
        print("5. Count Customers")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()
        match choice:
            case "1":
                add_customer()
            case "2":
                update_address()
            case "3":
                delete_customer()
            case "4":
                show_customers()
            case "5":
                count_customers()
            case "6":
                print("👋 Exiting. Goodbye!")
                break
            case _:
                print("❌ Invalid option. Try again.")

# Ejecutar programa
main_menu()
