# Persona Ideal

print("A continuación te ayudaremos a determinar qué tan buena es para ti la persona de la que estás enamorado/a.")

nombre_enamorado = input("Ingresa el nombre de esa persona: ")
puntaje = 100 


pregunta1 = input(f"¿{nombre_enamorado} es una buena persona? (si/no): ").strip().lower()
if pregunta1 == "no":
 print("- No es una buena persona, eso resta puntos.")
 puntaje -= 20


pregunta2 = input("¿Es una persona maleducada? (si/no): ").strip().lower()
if pregunta2 == "si":
 print("- La mala educación no es una buena señal.")
 puntaje -= 20


pregunta3 = input("¿Te escucha y te apoya cuando lo necesitas? (si/no): ").strip().lower()
if pregunta3 == "no":
 print("- No sentir apoyo emocional puede ser un problema.")
 puntaje -= 30

pregunta4 = input("¿Confías plenamente en esa persona? (si/no): ").strip().lower()
if pregunta4 == "no":
 print("- La confianza es clave en una relación.")
 puntaje -= 30


print(f"\nPuntaje final: {puntaje}/100")

if puntaje >= 80:
 print(f"{nombre_enamorado} parece ser una muy buena persona para ti.")
elif puntaje >= 60:
 print(f"{nombre_enamorado} tiene cosas buenas, pero también detalles por mejorar.")
else:
    print(f"{nombre_enamorado} quizás no sea la mejor opción para ti en este momento.")