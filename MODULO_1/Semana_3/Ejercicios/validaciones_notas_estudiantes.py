"""
Ejercicio 1: Registro de Estudiantes
Objetivo:
Crear un diccionario para almacenar información sobre estudiantes y realizar algunas operaciones básicas como agregar, modificar y mostrar datos.

Instrucciones:
Crea un diccionario llamado estudiantes, donde las claves sean los nombres de los estudiantes y los valores sean otro diccionario con las claves edad y calificacion.

El programa debe permitir al usuario realizar las siguientes operaciones:

Agregar un nuevo estudiante (nombre, edad, calificación).
Modificar la calificación de un estudiante.
Mostrar la información de todos los estudiantes.
Eliminar un estudiante por su nombre.

"""
# Main dictionary to store student information
students = {}

# Function to add a new student
def add_student():
    name = input("Enter the student's name: ").strip().title()

    # Check if student already exists
    if name in students:
        print(f"❌ Student {name} already exists.")
        return
    
    # Input student data: age
    try:
        age = int(input(f"Enter {name}'s age: "))
        if age < 1:
            print("❌ Age must be a positive number.")
            return
    except ValueError:
        print("❌ Invalid input. Please enter a valid age.")
        return

    # Input student's grade with validation
    while True:
        try:
            grade = float(input(f"Enter {name}'s grade (0 to 100): "))
            if grade < 0 or grade > 100:
                print("❌ Grade must be between 0 and 100. Please try again.")
                continue
            break  # Exit the loop if the grade is valid
        except ValueError:
            print("❌ Invalid input. Please enter a valid grade between 0 and 100.")

    # Add student to the dictionary
    students[name] = {"age": age, "grade": grade}
    print(f"✅ Student {name} added successfully!")

# Function to modify a student's grade
def modify_grade():
    name = input("Enter the name of the student to modify the grade: ").strip().title()

    if name not in students:
        print(f"❌ Student {name} not found.")
        return

    # Input new grade with validation
    while True:
        try:
            new_grade = float(input(f"Enter the new grade for {name} (0 to 100): "))
            if new_grade < 0 or new_grade > 100:
                print("❌ Grade must be between 0 and 100. Please try again.")
                continue
            students[name]["grade"] = new_grade
            print(f"✅ {name}'s grade updated successfully!")
            break  # Exit the loop once the grade is updated
        except ValueError:
            print("❌ Invalid input. Please enter a valid grade between 0 and 100.")

# Function to display all student information
def show_students():
    if not students:
        print("📭 No students found.")
        return

    for name, info in students.items():
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

# Function to delete a student by name
def delete_student():
    name = input("Enter the name of the student to delete: ").strip().title()

    if name not in students:
        print(f"❌ Student {name} not found.")
        return

    del students[name]
    print(f"✅ Student {name} deleted successfully.")

# Main menu function
def menu():
    while True:
        print("\n🎓 Student Registration Menu")
        print("1. Add New Student")
        print("2. Modify Student Grade")
        print("3. Show All Students")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        # Handle the user's menu choice
        if choice == "1":
            add_student()
        elif choice == "2":
            modify_grade()
        elif choice == "3":
            show_students()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

# Run the program
menu()

