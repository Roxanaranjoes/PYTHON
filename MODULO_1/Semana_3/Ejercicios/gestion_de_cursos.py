"""
Sistema de Gestión de Cursos
Descripción:
Crear un sistema que permita gestionar cursos en línea. Cada curso tiene un título, una duración (en horas) y un precio. Los usuarios pueden inscribirse en estos cursos.

Requisitos:

Permitir agregar un nuevo curso con título, duración y precio.

Permitir actualizar la duración o el precio de un curso.

Permitir eliminar un curso.

Mostrar todos los cursos disponibles.

Validar que el precio y la duración sean valores positivos.

Posibles preguntas:

¿Cómo manejarías la inscripción de estudiantes en un curso?

¿Cómo validarías que la duración del curso sea un número entero positivo?

Ejemplo de pregunta:
"Crea un sistema para gestionar cursos en línea. Permite agregar, actualizar y eliminar cursos, y mostrar todos los cursos disponibles. Asegúrate de que el precio y la duración sean números positivos."


"""
# Course Management System

# This list will hold all the courses
courses = []

# Function to add a new course
def add_course():
    print("\n📚 Add a New Course")
    title = input("Enter course title: ").strip().title()
    if not title:
        print("⚠️ Course title cannot be empty.")
        return

    try:
        duration = int(input("Enter course duration in hours: "))
        if duration <= 0:
            print("⚠️ Duration must be a positive integer.")
            return
    except ValueError:
        print("⚠️ Please enter a valid number for duration.")
        return

    try:
        price = float(input("Enter course price: "))
        if price <= 0:
            print("⚠️ Price must be a positive number.")
            return
    except ValueError:
        print("⚠️ Please enter a valid number for price.")
        return

    course = {
        "title": title,
        "duration": duration,
        "price": price,
        "students": []
    }

    courses.append(course)
    print(f"✅ Course '{title}' added successfully!")

# Function to enroll a student in a course
def enroll_student():
    print("\n👩‍🎓 Enroll a Student")
    if not courses:
        print("⚠️ No courses available.")
        return

    show_courses()
    title = input("Enter the title of the course to enroll in: ").strip().title()
    for course in courses:
        if course["title"] == title:
            student_name = input("Enter student name: ").strip().title()
            if student_name:
                course["students"].append(student_name)
                print(f"✅ {student_name} enrolled in '{title}'.")
            else:
                print("⚠️ Student name cannot be empty.")
            return

    print(f"⚠️ Course '{title}' not found.")

# Function to update course duration or price
def update_course():
    print("\n🔁 Update Course Info")
    if not courses:
        print("⚠️ No courses available.")
        return

    show_courses()
    title = input("Enter the title of the course to update: ").strip().title()
    for course in courses:
        if course["title"] == title:
            print(f"Current duration: {course['duration']} hours")
            print(f"Current price: ${course['price']:.2f}")

            try:
                new_duration = int(input("Enter new duration (or press Enter to skip): ") or course["duration"])
                if new_duration <= 0:
                    print("⚠️ Duration must be a positive integer.")
                    return
            except ValueError:
                print("⚠️ Invalid duration input.")
                return

            try:
                new_price = float(input("Enter new price (or press Enter to skip): ") or course["price"])
                if new_price <= 0:
                    print("⚠️ Price must be a positive number.")
                    return
            except ValueError:
                print("⚠️ Invalid price input.")
                return

            course["duration"] = new_duration
            course["price"] = new_price
            print(f"✅ Course '{title}' updated successfully.")
            return

    print(f"⚠️ Course '{title}' not found.")

# Function to delete a course
def delete_course():
    print("\n🗑️ Delete a Course")
    if not courses:
        print("⚠️ No courses to delete.")
        return

    show_courses()
    title = input("Enter the title of the course to delete: ").strip().title()
    for i, course in enumerate(courses):
        if course["title"] == title:
            courses.pop(i)
            print(f"🗑️ Course '{title}' deleted successfully.")
            return

    print(f"⚠️ Course '{title}' not found.")

# Function to show all courses
def show_courses():
    print("\n📋 List of All Courses")
    if not courses:
        print("⚠️ No courses registered.")
        return

    for idx, course in enumerate(courses, 1):
        print(f"{idx}. Title: {course['title']}")
        print(f"   Duration: {course['duration']} hours")
        print(f"   Price: ${course['price']:.2f}")
        print(f"   Students Enrolled: {', '.join(course['students']) if course['students'] else 'None'}")

# Main menu
def main():
    while True:
        print("\n==== COURSE MANAGEMENT MENU ====")
        print("1. Add Course")
        print("2. Enroll Student")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Show All Courses")
        print("6. Exit")

        choice = input("Select an option (1-6): ").strip()
        match choice:
            case "1":
                add_course()
            case "2":
                enroll_student()
            case "3":
                update_course()
            case "4":
                delete_course()
            case "5":
                show_courses()
            case "6":
                print("👋 Exiting the program. Goodbye!")
                break
            case _:
                print("❌ Invalid option. Please enter a number from 1 to 6.")

# Entry point
if __name__ == "__main__":
    main()
