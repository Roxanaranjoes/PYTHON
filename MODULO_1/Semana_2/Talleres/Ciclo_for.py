#Ejercicios para Practicar Ciclo for en Python

#1
print("Contar del 1 al 10")
for i in range(1,11):
    print(i)
    
#2 
print("Contar hacia atrás")
for i in range(10,1,-1):
    print(i)
    
#3    
print("Sumar los primeros 10 números")
suma1=0
for i in range(1,11):
    suma1+=i
    print(suma1)

#4
print("Números pares del 1 al 20")
for i in range(2,21,2):
    print(i)

#5
print("Detectar múltiplos de 3")
for i in range(1,31):
    if i%3==0:
        print(i)

#6
print("Contar letras a")
palabra1=input("Ingrese una palabra: ").lower()
contador2=0
for letra in palabra1:
    if letra=="a":
        contador2+=1
print(f"La letra a aparece {contador2} veces en {palabra1}")

#7
print("Tabla de multiplicar del 5")
contador3=1
for i in range(1,11): 
    print(f"{i} x 5 = {i*5}")
    
#8
print("Números positivos en una lista")
lista1=[3, -1, 5, -2, 7, -8]
for i in lista1:
    if i>0:
     print(i)

#9
print("Mayúsculas y minúsculas")
palabra4=input("Ingrese una palabra: ")
mayus=0
minus=0
for letra in palabra4:
    if letra.isupper():
        mayus+=1
    elif letra.islower():
        minus+=1
print(f"En la palabra {palabra4} hay {mayus} letra(s) mayúsculas y {minus} letra(s) minúsculas")

#10
print("Simulación de contraseña")

contraseña_correcta="python123"

for intento in range(3):
    contraseña=input("Ingrese su contrseña: ")
    if contraseña== contraseña_correcta:
        print("Acceso permitido")
        break
    else:
        print("Contraseña incorrecta")
else:
    print("Acceso denegado. No hay más intentos")     