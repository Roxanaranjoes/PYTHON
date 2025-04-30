#Conducir

edad = int(input("¿Cuál es tu edad? "))
licencia = input("¿Tienes licencia de conducción? (si/no): ").lower()

if edad >= 18 and licencia == "si":
    print("Puedes conducir")
else:
    print("No puedes conducir")
