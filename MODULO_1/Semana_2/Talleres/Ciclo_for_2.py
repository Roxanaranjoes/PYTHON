# Ejercicio 1: Imprimir caracteres de una cadena
def imprimir_caracteres():
    cadena = input("Ingresa una cadena de texto: ")
    for caracter in cadena:
        print(caracter)

# Ejercicio 2: Sumar los números en una lista
def sumar_numeros_en_lista():
    lista = [1, 2, 3, 4, 5]
    suma = 0
    for numero in lista:
        suma += numero
    print("La suma de los números es:", suma)

# Ejercicio 3: Números impares del 1 al 30
def numeros_impares():
    for numero in range(1, 31):
        if numero % 2 != 0:
            print(numero)

# Ejercicio 4: Encontrar la letra más frecuente
def letra_mas_frecuente():
    palabra = input("Ingresa una palabra: ")
    frecuencia = {}
    for letra in palabra:
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1

    letra_max = max(frecuencia, key=frecuencia.get)
    print(f"La letra más frecuente es: {letra_max}")

# Ejercicio 5: Verificar si un número es primo
def verificar_primo():
    numero = int(input("Ingresa un número: "))
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo and numero > 1:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")

# Ejercicio 6: Sumar números negativos
def sumar_numeros_negativos():
    lista = [4, -2, -6, 7, -3]
    suma_negativos = 0
    for numero in lista:
        if numero < 0:
            suma_negativos += numero
    print("La suma de los números negativos es:", suma_negativos)

# Ejercicio 7: Contar palabras con más de 3 letras
def contar_palabras_mayores_3():
    oracion = input("Ingresa una oración: ")
    palabras = oracion.split()
    contador = 0
    for palabra in palabras:
        if len(palabra) > 3:
            contador += 1
    print(f"El número de palabras con más de 3 letras es: {contador}")

# Ejercicio 8: Imprimir los primeros N números
def imprimir_primeros_n():
    n = int(input("Ingresa un número N: "))
    for numero in range(n):
        print(numero)

# Ejercicio 9: Número mayor en una lista
def numero_mayor_en_lista():
    lista = [10, 2, 30, 4]
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    print(f"El número mayor en la lista es: {mayor}")

# Ejercicio 10: Divisores de un número
def divisores_de_un_numero():
    numero = int(input("Ingresa un número: "))
    print(f"Los divisores de {numero} son:")
    for i in range(1, numero):
        if numero % i == 0:
            print(i)

# Menú principal para ejecutar los ejercicios
def menu_principal():
    while True:
        print("\nElige el ejercicio que quieres ejecutar:")
        print("1. Imprimir caracteres de una cadena")
        print("2. Sumar los números en una lista")
        print("3. Números impares del 1 al 30")
        print("4. Encontrar la letra más frecuente")
        print("5. Verificar si un número es primo")
        print("6. Sumar números negativos")
        print("7. Contar palabras con más de 3 letras")
        print("8. Imprimir los primeros N números")
        print("9. Número mayor en una lista")
        print("10. Divisores de un número")
        print("0. Salir")

        opcion = int(input("Elige una opción (0-10): "))

        if opcion == 0:
            print("¡Hasta luego!")
            break
        elif opcion == 1:
            imprimir_caracteres()
        elif opcion == 2:
            sumar_numeros_en_lista()
        elif opcion == 3:
            numeros_impares()
        elif opcion == 4:
            letra_mas_frecuente()
        elif opcion == 5:
            verificar_primo()
        elif opcion == 6:
            sumar_numeros_negativos()
        elif opcion == 7:
            contar_palabras_mayores_3()
        elif opcion == 8:
            imprimir_primeros_n()
        elif opcion == 9:
            numero_mayor_en_lista()
        elif opcion == 10:
            divisores_de_un_numero()
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú principal
menu_principal()
