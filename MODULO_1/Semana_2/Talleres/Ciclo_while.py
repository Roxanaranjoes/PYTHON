# Función para contar del 1 al 10
def contar_del_1_al_10():
    contador = 1
    while contador <= 10:
        print(contador)
        contador += 1

# Función para contar hacia atrás desde 10 hasta 1
def contar_hacia_atras():
    contador = 10
    while contador >= 1:
        print(contador)
        contador -= 1

# Función para sumar los primeros 10 números
def suma_de_los_primeros_10():
    contador = 1
    suma = 0
    while contador <= 10:
        suma += contador
        contador += 1
    print("La suma de los primeros 10 números es:", suma)

# Función para solicitar un número positivo
def solicitar_numero_positivo():
    numero = int(input("Ingresa un número positivo: "))
    while numero <= 0:
        print("El número no es positivo.")
        numero = int(input("Ingresa un número positivo: "))
    print("Número ingresado correctamente:", numero)

# Función para el menú interactivo
def menu_interactivo():
    opcion = 0
    while opcion != 3:
        print("\nMenú:")
        print("1. Saludar")
        print("2. Despedirse")
        print("3. Salir")
        opcion = int(input("Elige una opción (1, 2, 3): "))
        
        if opcion == 1:
            print("¡Hola!")
        elif opcion == 2:
            print("¡Adiós!")
        elif opcion == 3:
            print("Saliendo...")
        else:
            print("Opción no válida. Intenta de nuevo.")

# Función para adivinar un número secreto
def adivina_el_numero():
    numero_secreto = 7
    adivinanza = int(input("Adivina el número entre 1 y 10: "))
    while adivinanza != numero_secreto:
        if adivinanza < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        adivinanza = int(input("Adivina el número entre 1 y 10: "))
    print("¡Correcto! Has adivinado el número.")

# Función para contar las vocales en una palabra
def contar_vocales():
    palabra = input("Ingresa una palabra: ")
    vocales = "aeiou"
    contador_vocales = 0
    indice = 0

    while indice < len(palabra):
        if palabra[indice].lower() in vocales:
            contador_vocales += 1
        indice += 1

    print("La palabra tiene", contador_vocales, "vocales.")

# Función para validar la contraseña
def validar_contraseña():
    contraseña = input("Ingresa la contraseña: ")
    while contraseña != "python123":
        print("Contraseña incorrecta. Intenta de nuevo.")
        contraseña = input("Ingresa la contraseña: ")
    print("Contraseña correcta.")

# Función para sumar números hasta detenerse con 0
def sumar_hasta_detenerse():
    suma = 0
    numero = int(input("Ingresa un número (0 para terminar): "))
    while numero != 0:
        suma += numero
        numero = int(input("Ingresa un número (0 para terminar): "))
    print("La suma total es:", suma)

# Función para pedir un número entre 1 y 10
def numero_de_intentos():
    numero = int(input("Ingresa un número entre 1 y 10: "))
    while numero < 1 or numero > 10:
        print("Número fuera de rango. Intenta de nuevo.")
        numero = int(input("Ingresa un número entre 1 y 10: "))
    print("Número ingresado correctamente:", numero)

# Función principal para mostrar el menú y ejecutar las opciones
def menu_principal():
    while True:
        print("\nElige el ejercicio que quieres ejecutar:")
        print("1. Contar del 1 al 10")
        print("2. Contar hacia atrás")
        print("3. Suma de los primeros 10 números")
        print("4. Solicitar número positivo")
        print("5. Menú interactivo")
        print("6. Adivina el número")
        print("7. Contar vocales en una palabra")
        print("8. Validar contraseña")
        print("9. Sumar hasta detenerse")
        print("10. Número de intentos")
        print("0. Salir")

        opcion = int(input("Elige una opción (0-10): "))

        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            contar_del_1_al_10()
        elif opcion == 2:
            contar_hacia_atras()
        elif opcion == 3:
            suma_de_los_primeros_10()
        elif opcion == 4:
            solicitar_numero_positivo()
        elif opcion == 5:
            menu_interactivo()
        elif opcion == 6:
            adivina_el_numero()
        elif opcion == 7:
            contar_vocales()
        elif opcion == 8:
            validar_contraseña()
        elif opcion == 9:
            sumar_hasta_detenerse()
        elif opcion == 10:
            numero_de_intentos()
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecución del menú principal
menu_principal()
