# Conversor de minutos a días y horas

minutos = int(input("Ingrese la cantidad de minutos: "))

dias = minutos // 1440 

horas = (minutos % 1440) // 60

minutosrestantes = (minutos % 1440) % 60

print(f"{dias} días, {horas} horas, {minutosrestantes} minutos")
