"""Ejercicio: Gestión de  Contactos en una Agenda
Una agenda de contactos que tiene:
- Una lista de direcciones donde cada direccion es un diccionario con información sobre la calle y la ciudad, y 
código postal
-Almacenamos todo en un diccionario, el nombre del contacto será clave principal y los valores 
serán a su vez otros diccionarios con la información del télefono y las direcciones

"""

""" PASO 1: PREPARAR EL ENTORNO
Primero, vamos a preparar una variable vacía para almacenar nuestros contactos.
Es importante que los datos se mantencgan de manera ordenada.
"""

#Inicializamos una agenda vacía que va a alamacenar nuestros contactos
agenda={}

""" Explicación 
-agenda es un diccionario  vacío donde vamos aguardar cada contacto. El nombre del contacto será la clave (key)
y la información del contacto ( teléfono y direcciones) será el valor (value)

Se ve más o menos así, así se añadiría un contacto si no se le piese al usuario

agenda["John Doe"] = {
    "phone": "123-456-7890",
    "addresses": [
        {"street": "123 Elm St", "city": "Somewhere", "zip": "12345"},
        {"street": "456 Oak St", "city": "Anywhere", "zip": "67890"}
    ]
}
"""
"""PASO 2: CREAR UN NUEVO CONTACTO (FUNCIÓN "CREAR")
Ahora vamos a crear una función llamada create_contact que permitirá agregar un
nuevo contacto a la agenda.

2.1: Solicitar al usuario los datos:
Dentro de la función vamos a pedirle al usuario que ingrese:
 1. El nombre del contacto.
 2. El númerro de teléfono del contacto.
 3. La direcciones del contacto.

"""
def create_contact():
    name = input("Enter the name of the contact: ").strip().title()

    if name in agenda:
        print(f"❌ Contact '{name}' already exists.")
        return

    # --- Phone Validation ---
    phone = input("Enter the phone number: ").strip()
    if not phone.isdigit():
        print("❌ Phone number must contain only digits.")
        return

    # --- Birth Date Validation ---
    errors = 0
    max_errors = 5
    while errors < max_errors:
        birth = input("Enter date of birth (dd/mm/yyyy): ").strip()
        parts = birth.split("/")

        if len(parts) != 3:
            print("⚠️ Incorrect format. Use dd/mm/yyyy.")
            errors += 1
            continue

        day, month, year = parts
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            print("⚠️ All parts must be numbers.")
            errors += 1
            continue

        day, month, year = int(day), int(month), int(year)
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2025):
            print("⚠️ Invalid date. Please try again.")
            errors += 1
            continue

        break  # Fecha válida

    if errors == max_errors:
        print("❌ Too many errors. Contact not created.")
        return

    # --- Addresses Entry ---
    addresses = []
    while True:
        street = input("Enter the street address (or type 'Done' to finish): ").strip().title()
        if street.lower() == "done":
            break
        if not street:
            print("⚠️ Street cannot be empty.")
            continue

        city = input("Enter the city: ").strip().title()
        if not city:
            print("⚠️ City cannot be empty.")
            continue

        zip_code = input("Enter the zip code (6 digits): ").strip()
        if not zip_code.isdigit() or len(zip_code) != 6:
            print("⚠️ Zip code must contain exactly 6 digits.")
            continue

        # Add validated address
        addresses.append({
            "street": street,
            "city": city,
            "zip code": zip_code
        })

    # --- Final Contact Creation ---
    agenda[name] = {
        "phone": phone,
        "birth": birth,
        "addresses": addresses
    }

    print(f"✅ Contact '{name}' has been successfully created.")

 
""" Explicación:
- name: El nombre del contacto será la clave en el diccionario.
- phone: Pedimos el teléfono del contacto. Verificamos que solo sea números con .isdigit().
- addresses Creamos una lista vacía llamada addresses. Luego, pedimos 
al usuario que ingrese varias direcciones. Si el usuario escribe "done", termina de ingresar direcciones.
- agenda[name]: Guardamos la información del contacto en la agenda, donde el nombre es la clave y la información (teléfono y direcciones)
es el valos

# ✅ Validación del número de teléfono
    phone_errors = 0
    max_errors = 5
    while phone_errors < max_errors:
        phone = input("Enter phone number: ")
        if phone.isdigit() and len(phone) > 0:
            break
        else:
            print("⚠️ Phone must contain only digits.")
            phone_errors += 1
    if phone_errors == max_errors:
        print("❌ Too many errors with phone. Contact not created.")
        return
# ✅ Validación del código postal (ZIP code)
zip_errors = 0
while zip_errors < max_errors:
    zip_code = input("Enter ZIP code (6 digits): ")
    if zip_code.isdigit() and len(zip_code) == 6:
        break
    else:
        print("⚠️ ZIP code must be exactly 6 digits.")
        zip_errors += 1
if zip_errors == max_errors:
    print("❌ Too many errors with ZIP code. Contact not created.")
    return

"""

"""PASO 3: LEER UN CONTACTO (FUNCIÓN "LEER")
Ahora vamos a crear una función llamada read_contact() que permitirá consultar la información de un
contacto que ya está en la agenda.
"""
def read_contact():

    #Pedimos el nombre del contacto

    name= input(" Enter the name of the contact to search: ").strip().title()
    
    #Verificamos si el contacto existe en la agenda 
    if name in agenda:
        contact= agenda[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Birth date: {contact['birth']}")
        print("Addresses: ")

        # Mostramos todas las direcciones asociadas al contacto
        for address in contact["addresses"]:
            print(f" Street: {address['street']}, City: {address['city']}, Zip Code: {address['zip code']}")

    else:
        print("Contact not found!")

"""
Explicación:
- Pedimos el nombre del contacto y verificamos si está en la agenda usando if name in agenda
- Si el contacto existe, mostramos su télefono y todas las direcciones
- Si el contacto no existe mostramos un mensaje de error

"""
"""
PASO 4: ACTUALIZAR UN CONTACTO (FUNCIÓN "ACTUALIZAR")
Ahora vamos a permitir al usuario actuaalizar el teléfono o las direcciones de un contacto
existente


"""
def update_contact():
    name = input("Enter the name of the contact to update: ").strip().title()

    if name not in agenda:
        print(f"❌ Contact '{name}' not found!")
        return

    contact = agenda[name]
    updated = False  # bandera para confirmar si algo fue actualizado

    # --- Phone Update ---
    phone_choice = input("Do you want to update the phone number? (yes/no): ").strip().lower()
    while phone_choice not in ("yes", "no"):
        phone_choice = input("⚠️ Please type 'yes' or 'no': ").strip().lower()
    if phone_choice == "yes":
        new_phone = input(f"Enter new phone number for {name} (current: {contact['phone']}): ")
        if new_phone.isdigit():
            contact["phone"] = new_phone
            print("✅ Phone number updated.")
            updated = True
        else:
            print("❌ Phone number must contain only digits.")

    # --- Birth Date Update ---
    birth_choice = input("Do you want to update the birth date? (yes/no): ").strip().lower()
    while birth_choice not in ("yes", "no"):
        birth_choice = input("⚠️ Please type 'yes' or 'no': ").strip().lower()
    if birth_choice == "yes":
        errors = 0
        max_errors = 5
        while errors < max_errors:
            birth_new = input(f"Enter new date of birth for {name} in dd/mm/yyyy (current: {contact['birth']}): ")
            parts = birth_new.split("/")

            if len(parts) != 3:
                print("⚠️ Incorrect format. Use dd/mm/yyyy.")
                errors += 1
                continue

            day, month, year = parts
            if not (day.isdigit() and month.isdigit() and year.isdigit()):
                print("⚠️ All parts must be numbers.")
                errors += 1
                continue

            day, month, year = int(day), int(month), int(year)
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2025):
                print("⚠️ Invalid date. Please try again.")
                errors += 1
                continue

            contact["birth"] = birth_new
            print("✅ Birth date updated.")
            updated = True
            break

        if errors == max_errors:
            print("❌ Too many errors. Birth date not updated.")

    # --- Address Update ---
    print("\nCurrent addresses:")
    for i, address in enumerate(contact["addresses"], 1):
        print(f"{i}. {address['street']}, {address['city']}, {address['zip code']}")

    address_choice = input("Do you want to update an address? (yes/no): ").strip().lower()
    while address_choice not in ("yes", "no"):
        address_choice = input("⚠️ Please type 'yes' or 'no': ").strip().lower()

    if address_choice == "yes":
        try:
            index = int(input(f"Enter address number to update (1 to {len(contact['addresses'])}): ")) - 1
            if 0 <= index < len(contact["addresses"]):
                street = input("New street: ").strip()
                city = input("New city: ").strip()

                zip_code = input("New zip code (6 digits): ").strip()
                if not zip_code.isdigit() or len(zip_code) != 6:
                    print("❌ Zip code must be exactly 6 digits.")
                else:
                    contact["addresses"][index] = {
                        "street": street,
                        "city": city,
                        "zip code": zip_code
                    }
                    print("✅ Address updated.")
                    updated = True
            else:
                print("❌ Invalid address number.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
    else:
        print("ℹ️ Address not updated.")

    # --- Final Message ---
    if updated:
        print(f"\n✅ Contact '{name}' has been successfully updated.")
    else:
        print(f"\nℹ️ No changes were made to the contact '{name}'.")

"""Explicación:
- Si el contacto existe le pedimos que ingrese un nuevo télefono.
- Luego, mostramos las direcciones actuales y preguntamos al usuario si quiere actualizar alguna dirección.
- Si el usuario dice que sí, le pedimos que seleccione el número de la dirección a actualizar (validamos que este dentro del rango).
- Finalmente, actualizamos la dirección seleccionada.
"""
"""PASO 5: ELIMINAR UN CONTACTO (FUNCIÓN ELIMINAR)
Finalmente, vamos a crear una función para eliminar un contacto.
"""
def delete_contact(): 
    name=input("Enter the name of the contact to delete ").strip().title()

    #Verificamos si el contacto existe
    if name in agenda:
        del agenda[name]
        print(f"Contact {name} has been deleted. ")
    else:
        print(f"Contact {name} not found! ")

"""Explicación:
- Si el contacto existe, lo eliminamos con del agenda[name].
- Si el contacto no está en la agenda, mostramos un mensaje diciendo que no se encontró.

"""
"""
PASO 6: MENÚ INTERACTIVO
Finalmente, vamos a crear un menú interactivo para que el usuario pueda seleccionar lo que va a hacer.
"""

def menu():
    while True:
        print("\n----- Contact Management System -----")
        print("1. Add new contact (Create)")
        print("2. View contact information (Read)")
        print("3. Update contact information (Update)")
        print("4. Delete contact (Delete)")
        print("5. Exit")

        choice= input("Select an option (1-5): ")

        match choice:

            case "1":
                create_contact()
            case "2":
                read_contact()
            case "3":
                update_contact()
            case "4":
                delete_contact()
            case "5":
                print("Exiting the program.")
                break
            case _:
                print("Invalid option! Please  choose a number berween 1 and 5.")

"""Explicación:
- El menú permite al usuario elegir qué acción desea realizar.
- Usamos un match para que el usuario seleccione una opción, que ejecutará la función correspondiente.

"""
menu()