# Ejercicio Gestión de Animales

print("Bienvenido a la veterinaria Pecas")

nombres = []
edades = []
salud = []

def agregar_animal():
    global nombres, edades, salud  # Declarar variables globales
    while True:
        try:
            nombreanimal = input("Ingrese el nombre del animal: ")

            # Validar que la edad sea un número entero
            edad = int(input("Ingrese la edad del animal: "))
            
            # Preguntar si el animal está enfermo
            enfermo = input("¿El animal está enfermo? (si/no): ").lower()
            
            # Validar respuesta de enfermo
            if enfermo not in ["si", "no"]:
                print("Por favor, responde 'si' o 'no'.")
                continue
            
            # Agregar datos a las listas globales
            nombres.append(nombreanimal)
            edades.append(edad)
            salud.append("Enfermo" if enfermo == "si" else "Sano")
            
            # Confirmar que el animal fue agregado
            print(f"Animal agregado: {nombreanimal}, Edad: {edad}, Enfermo: {enfermo}")
            break
        except ValueError:
            print("Error: La edad debe ser un número entero. Inténtalo de nuevo.")

def mostrar_animales():
    global nombres, edades, salud  # Declarar variables globales
    if not nombres:
        print("\nNo hay animales en la lista")
        return
    print("\nLista de animales:")
    for i in range(len(nombres)):
        estado = "enfermo" if salud[i] == "Enfermo" else "sano"
        print(f"Nombre: {nombres[i]}, Edad: {edades[i]}, Estado: {estado}")

def eliminar_animales():
    global nombres, edades, salud  # Declarar variables globales
    nombreanimal = input("Ingrese el nombre del animal: ")
    if nombreanimal not in nombres:
        print("No se encontró el animal ingresado")
        return
    else:
        indice = nombres.index(nombreanimal)
        nombres.pop(indice)
        edades.pop(indice)
        salud.pop(indice)
        print(f"El animal {nombreanimal} ha sido eliminado del sistema")

def menu_principal():
    while True:
        print("\nElige una opción que quiera usted ejecutar:")
        print("1. Agregar animal al sistema")
        print("2. Mostrar animales en el sistema")
        print("3. Eliminar animal del sistema")
        print("0. Salir")
        
        try:
            opcion = int(input("Elige una opción (0-3): "))
            match opcion:
                case 0:
                    print("¡Hasta luego!")
                    break
                case 1:
                    agregar_animal()
                case 2:
                    mostrar_animales()
                case 3:
                    eliminar_animales()
                case _:
                    print("Opción no válida, intenta de nuevo")
        except ValueError:
            print("Error: Debes ingresar un número entre 0 y 3.")

menu_principal()

        
    