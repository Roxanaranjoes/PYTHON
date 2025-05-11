
"""
Sistema de Reservas (Ejemplo: Restaurante o Hotel)
Descripción:
Crear un sistema de reservas donde puedas gestionar las reservas de mesas o habitaciones.

Requisitos:

Permitir al usuario agregar una nueva reserva con detalles como nombre del cliente, fecha y hora, número de personas.

Permitir modificar los detalles de una reserva existente.

Permitir eliminar una reserva.

Mostrar todas las reservas registradas.

Validar que la fecha y hora ingresadas sean correctas y que el número de personas no sea negativo.

Posibles preguntas:

¿Cómo manejarías la validación de fechas?

¿Cómo comprobarías si una fecha ya tiene una reserva?

Ejemplo de pregunta:
"Imagina que estás creando un sistema para gestionar las reservas de un restaurante. Crea un programa donde puedas agregar, modificar y eliminar reservas, y mostrar todas las reservas. La reserva debe tener nombre del cliente, fecha, hora y número de personas."
"""


# List to store all reservations
reservations = []

# Maximum number of input errors allowed
max_errors = 5

def add_reservation():
    print("\n📌 Add a New Reservation")
    name = input("Enter customer's name: ").strip().title()
    if not name:
        print("❌ Name cannot be empty.")
        return

    # Validate date in format dd/mm/yyyy
    errors = 0
    while errors < max_errors:
        date = input("Enter reservation date (dd/mm/yyyy): ").strip()
        parts = date.split("/")
        if len(parts) != 3:
            print("⚠️ Incorrect format. Use dd/mm/yyyy.")
            errors += 1
            continue
        day, month, year = parts
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            print("⚠️ All parts must be numbers.")
            errors += 1
            continue
        day = int(day)
        month = int(month)
        year = int(year)
        if not (1 <= day <= 31 and 1 <= month <= 12 and 2024 <= year <= 2030):
            print("⚠️ Invalid date.")
            errors += 1
            continue
        break
    else:
        print("❌ Too many errors. Reservation not added.")
        return

    # Validate hour (24h format)
    hour = input("Enter reservation hour (HH:MM, 24h format): ").strip()
    if ":" not in hour:
        print("❌ Hour format must be HH:MM.")
        return

    # Validate number of people
    people = input("Enter number of people: ").strip()
    if not people.isdigit() or int(people) <= 0:
        print("❌ Invalid number of people.")
        return

    # Check for existing reservation at same date and hour
    for r in reservations:
        if r["date"] == date and r["hour"] == hour:
            print("⚠️ There's already a reservation at this date and hour.")
            return

    # Add reservation
    reservations.append({
        "name": name,
        "date": date,
        "hour": hour,
        "people": int(people)
    })
    print("✅ Reservation added successfully!")

def view_reservations():
    print("\n📋 All Reservations")
    if not reservations:
        print("No reservations found.")
        return
    for idx, r in enumerate(reservations, 1):
        print(f"{idx}. {r['name']} - {r['date']} at {r['hour']} for {r['people']} people")

def update_reservation():
    view_reservations()
    if not reservations:
        return
    try:
        index = int(input("Enter the reservation number to update: ")) - 1
        if 0 <= index < len(reservations):
            r = reservations[index]
            print(f"Updating reservation for {r['name']}")
            new_name = input(f"New name (leave empty to keep '{r['name']}'): ").strip().title()
            if new_name:
                r["name"] = new_name

            new_date = input(f"New date (dd/mm/yyyy) (current: {r['date']}): ").strip()
            if new_date:
                parts = new_date.split("/")
                if len(parts) == 3 and all(p.isdigit() for p in parts):
                    day, month, year = map(int, parts)
                    if 1 <= day <= 31 and 1 <= month <= 12 and 2024 <= year <= 2030:
                        r["date"] = new_date
                    else:
                        print("⚠️ Invalid date. Keeping old date.")
                else:
                    print("⚠️ Invalid format. Keeping old date.")

            new_hour = input(f"New hour (HH:MM) (current: {r['hour']}): ").strip()
            if new_hour:
                if ":" in new_hour:
                    r["hour"] = new_hour
                else:
                    print("⚠️ Invalid hour format. Keeping old hour.")

            new_people = input(f"New number of people (current: {r['people']}): ").strip()
            if new_people.isdigit() and int(new_people) > 0:
                r["people"] = int(new_people)
            elif new_people:
                print("⚠️ Invalid number. Keeping old value.")
            print("✅ Reservation updated.")
        else:
            print("❌ Invalid reservation number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_reservation():
    view_reservations()
    if not reservations:
        return
    try:
        index = int(input("Enter the reservation number to delete: ")) - 1
        if 0 <= index < len(reservations):
            removed = reservations.pop(index)
            print(f"🗑️ Reservation for {removed['name']} deleted.")
        else:
            print("❌ Invalid reservation number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Main interactive menu
def menu():
    while True:
        print("\n--- 🏨 Reservation System Menu ---")
        print("1. Add reservation")
        print("2. View all reservations")
        print("3. Update a reservation")
        print("4. Delete a reservation")
        print("5. Exit")

        option = input("Choose an option (1-5): ")
        match option:
            case "1":
                add_reservation()
            case "2":
                view_reservations()
            case "3":
                update_reservation()
            case "4":
                delete_reservation()
            case "5":
                print("👋 Goodbye!")
                break
            case _:
                print("❌ Invalid option. Please choose between 1 and 5.")

# Start program
menu()
