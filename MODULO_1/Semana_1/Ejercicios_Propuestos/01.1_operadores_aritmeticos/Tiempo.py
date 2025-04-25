# Extraer hora, minuto y segundo de segundos totales

segundostotales = int(input("Ingresa el número de segundos: "))

horas = segundostotales // 3600
segundosr = segundostotales % 3600
minutos = segundosr // 60
segundos = segundosr % 60

print(f"{segundostotales} segundos son: {horas} hora(s), {minutos} minuto(s), {segundos} segundo(s).")
