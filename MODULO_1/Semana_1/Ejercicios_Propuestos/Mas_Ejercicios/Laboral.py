#Experiencia Laboral y titulo universitario

experiencia_laboral = input("¿Tienes experiencia laboral? (si/no): ").lower()
titulo_universitario = input("¿Tienes título universitario? (si/no): ").lower()

if experiencia_laboral == "si" and titulo_universitario == "si":
    print("Puedes aplicar a la oferta de trabajo")
else:
    print("No cumples con los requisitos")
