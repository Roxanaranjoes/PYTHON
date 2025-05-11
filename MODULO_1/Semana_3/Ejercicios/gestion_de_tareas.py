"""
1. Gestión de Tareas o Proyecto (To-Do List)
Descripción:
Crear una lista de tareas (to-do list) donde puedas agregar, marcar como completada, eliminar o listar todas las tareas.

Requisitos:

Cada tarea tiene un título, una descripción y un estado (completa o pendiente).

Permitir agregar tareas con un título y una descripción.

Permitir actualizar el estado de la tarea (de pendiente a completada).

Permitir eliminar una tarea de la lista.

Mostrar todas las tareas con su título, descripción y estado.

Posibles preguntas:

¿Cómo manejarías las tareas pendientes y completadas?

¿Cómo validarías que el título de la tarea no esté vacío?

Ejemplo de pregunta:
"Imagina que estás creando una aplicación de lista de tareas. Crea un programa donde puedas agregar, actualizar, eliminar y mostrar todas las tareas. Además, agrega una validación para que el título de la tarea no quede vacío."
"""

# 📝 List to store all tasks
tasks = []

# ➕ Function to add a new task
def add_task():
    print("\n--- Add New Task ---")
    title = input("Enter the task title: ").strip()
    
    # ✅ Validate that title is not empty
    if not title:
        print("⚠️ Task title cannot be empty.")
        return

    description = input("Enter the task description: ").strip()

    # 🟡 Create the task dictionary with default status as 'pending'
    task = {
        "title": title,
        "description": description,
        "status": "pending"
    }

    tasks.append(task)
    print(f"✅ Task '{title}' added successfully.")

# 🧾 Function to show all tasks
def show_tasks():
    print("\n--- All Tasks ---")
    if not tasks:
        print("No tasks available.")
        return

    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. Title: {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Status: {task['status'].capitalize()}")

# ✅ Function to update task status to 'completed'
def mark_task_completed():
    print("\n--- Mark Task as Completed ---")
    if not tasks:
        print("No tasks to update.")
        return

    show_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            if tasks[task_num - 1]["status"] == "completed":
                print("Task is already marked as completed.")
            else:
                tasks[task_num - 1]["status"] = "completed"
                print("✅ Task marked as completed.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# ❌ Function to delete a task
def delete_task():
    print("\n--- Delete a Task ---")
    if not tasks:
        print("No tasks to delete.")
        return

    show_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"✅ Task '{removed['title']}' deleted.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

# 📋 Menu system
def menu():
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add task")
        print("2. Show all tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please enter a number from 1 to 5.")

# 🚀 Start the program
menu()
