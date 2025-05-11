"""
Sistema de Gestión de Tareas Colaborativas
Descripción:
Crear un sistema para gestionar tareas colaborativas en un equipo de trabajo. Cada tarea tendrá un título, descripción, responsable (quién es el encargado), fecha de vencimiento, y un estado (pendiente, en progreso, completada). Los usuarios podrán agregar, modificar, eliminar tareas y ver todas las tareas pendientes y completadas. Además, se debe permitir asignar responsables a cada tarea y verificar la validez de las fechas.

Requisitos:
Permitir agregar una nueva tarea con título, descripción, responsable, fecha de vencimiento y estado.

Permitir modificar el estado de la tarea o reasignar el responsable.

Permitir eliminar una tarea del sistema.

Mostrar todas las tareas con su título, descripción, responsable, fecha de vencimiento y estado.

Validar que la fecha de vencimiento sea válida (en formato dd/mm/yyyy).

Validar que el estado solo pueda ser "pendiente", "en progreso" o "completada".

Permitir que las tareas sean asignadas a un responsable, quien será un miembro del equipo (lista de usuarios predefinida).
"""

# Lista de tareas
tareas = []

# Lista de miembros del equipo
miembros_equipo = ["Ana", "Luis", "Carlos", "Marta", "Pedro"]

# Función para validar el formato de la fecha
def es_fecha_valida(fecha):
    try:
        dia, mes, año = map(int, fecha.split('/'))
        if 1 <= dia <= 31 and 1 <= mes <= 12 and 1900 <= año <= 2025:
            return True
        return False
    except ValueError:
        return False

# Función para validar que el estado de la tarea sea válido
def es_estado_valido(estado):
    return estado.lower() in ["pendiente", "en progreso", "completada"]

# Función para agregar una nueva tarea
def agregar_tarea():
    print("\n--- Agregar Nueva Tarea ---")
    titulo = input("Título de la tarea: ").strip()
    
    while len(titulo) == 0:
        print("⚠️ El título no puede estar vacío.")
        titulo = input("Título de la tarea: ").strip()

    descripcion = input("Descripción de la tarea: ").strip()
    
    while len(descripcion) == 0:
        print("⚠️ La descripción no puede estar vacía.")
        descripcion = input("Descripción de la tarea: ").strip()

    responsable = input(f"Responsable de la tarea (miembros disponibles: {', '.join(miembros_equipo)}): ").strip()
    
    while responsable not in miembros_equipo:
        print(f"⚠️ El responsable debe ser uno de los siguientes: {', '.join(miembros_equipo)}.")
        responsable = input(f"Responsable de la tarea (miembros disponibles: {', '.join(miembros_equipo)}): ").strip()

    fecha_vencimiento = input("Fecha de vencimiento (dd/mm/yyyy): ").strip()
    
    while not es_fecha_valida(fecha_vencimiento):
        print("⚠️ La fecha debe estar en el formato dd/mm/yyyy y ser válida.")
        fecha_vencimiento = input("Fecha de vencimiento (dd/mm/yyyy): ").strip()

    estado = input("Estado de la tarea (pendiente, en progreso, completada): ").strip().lower()
    
    while not es_estado_valido(estado):
        print("⚠️ El estado debe ser uno de los siguientes: pendiente, en progreso, completada.")
        estado = input("Estado de la tarea (pendiente, en progreso, completada): ").strip().lower()

    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "responsable": responsable,
        "fecha_vencimiento": fecha_vencimiento,
        "estado": estado
    }
    
    tareas.append(tarea)
    print(f"Tarea '{titulo}' agregada con éxito.")

# Función para mostrar todas las tareas
def mostrar_tareas():
    print("\n--- Todas las Tareas ---")
    if not tareas:
        print("No hay tareas registradas.")
        return
    
    for idx, tarea in enumerate(tareas, 1):
        print(f"{idx}. Título: {tarea['titulo']}, Responsable: {tarea['responsable']}, Fecha: {tarea['fecha_vencimiento']}, Estado: {tarea['estado']}")
        print(f"   Descripción: {tarea['descripcion']}")
        print()

# Función para modificar el estado de una tarea o reasignar el responsable
def modificar_tarea():
    mostrar_tareas()
    if not tareas:
        return

    try:
        id_tarea = int(input("\nIngrese el número de la tarea a modificar: ")) - 1
        if id_tarea < 0 or id_tarea >= len(tareas):
            print("⚠️ Tarea no encontrada.")
            return
        
        opcion = input("¿Qué desea modificar? (1) Estado (2) Responsable: ").strip()
        
        if opcion == "1":
            nuevo_estado = input("Nuevo estado de la tarea (pendiente, en progreso, completada): ").strip().lower()
            while not es_estado_valido(nuevo_estado):
                print("⚠️ El estado debe ser uno de los siguientes: pendiente, en progreso, completada.")
                nuevo_estado = input("Nuevo estado de la tarea (pendiente, en progreso, completada): ").strip().lower()
            tareas[id_tarea]['estado'] = nuevo_estado
            print(f"Estado de la tarea '{tareas[id_tarea]['titulo']}' actualizado.")
        
        elif opcion == "2":
            nuevo_responsable = input(f"Nuevo responsable de la tarea (miembros disponibles: {', '.join(miembros_equipo)}): ").strip()
            while nuevo_responsable not in miembros_equipo:
                print(f"⚠️ El responsable debe ser uno de los siguientes: {', '.join(miembros_equipo)}.")
                nuevo_responsable = input(f"Nuevo responsable de la tarea (miembros disponibles: {', '.join(miembros_equipo)}): ").strip()
            tareas[id_tarea]['responsable'] = nuevo_responsable
            print(f"Responsable de la tarea '{tareas[id_tarea]['titulo']}' actualizado.")
        
        else:
            print("⚠️ Opción no válida.")
    
    except ValueError:
        print("⚠️ Ingrese un número válido.")

# Función para eliminar una tarea
def eliminar_tarea():
    mostrar_tareas()
    if not tareas:
        return
    
    try:
        id_tarea = int(input("\nIngrese el número de la tarea a eliminar: ")) - 1
        if id_tarea < 0 or id_tarea >= len(tareas):
            print("⚠️ Tarea no encontrada.")
            return
        tarea_eliminada = tareas.pop(id_tarea)
        print(f"Tarea '{tarea_eliminada['titulo']}' eliminada con éxito.")
    except ValueError:
        print("⚠️ Ingrese un número válido.")

# Función principal que ejecuta el menú
def menu():
    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Agregar Tarea")
        print("2. Mostrar Tareas")
        print("3. Modificar Tarea")
        print("4. Eliminar Tarea")
        print("5. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                agregar_tarea()
            elif opcion == 2:
                mostrar_tareas()
            elif opcion == 3:
                modificar_tarea()
            elif opcion == 4:
                eliminar_tarea()
            elif opcion == 5:
                print("¡Hasta luego!")
                break
            else:
                print("⚠️ Opción no válida. Intente nuevamente.")
        except ValueError:
            print("⚠️ Debe ingresar un número válido.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
