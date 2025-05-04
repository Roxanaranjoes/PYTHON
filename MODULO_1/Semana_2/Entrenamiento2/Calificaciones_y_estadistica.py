while True:# Pedir una calificación válida entre 0 y 100
    calificacion = int(input("Ingresa una calificación entre 0 y 100: "))
    if calificacion < 0 or calificacion > 100:
        print("Calificación inválida, intenta de nuevo.")
    elif calificacion >= 60:
        print("¡Aprobado!")
        break
    else:
        print("Reprobado.")
        break
while True: # Solicitar lista de calificaciones válidas
    entrada = input("Ingresa calificaciones separadas por comas: ")
    partes = entrada.split(",")
    calificaciones = []
    for n in partes:
        if n.strip().isdigit():
            num = int(n.strip())
            if 0 <= num <= 100:
                calificaciones.append(num)
    if calificaciones:
        break
    else:
        print("No ingresaste calificaciones válidas, intenta de nuevo.")
suma = 0 # Calcular el promedio
for cal in calificaciones: suma += cal
promedio = suma / len(calificaciones)
print("El promedio es:", promedio)
valor = int(input("Ingresa un valor para comparar: "))# Contar calificaciones mayores que un valor dado
i = 0; mayores = 0
while i < len(calificaciones):
    if calificaciones[i] > valor: mayores += 1
    i += 1
print("Hay", mayores, "calificaciones mayores que", valor)
buscada = int(input("Ingresa la calificación a buscar: "))# Contar cuántas veces aparece una calificación específica
veces = 0
for cal in calificaciones:
    if cal == buscada: veces += 1; continue
    if cal > 100: break
print("La calificación", buscada, "aparece", veces, "veces")


