#10 Ejercicios para Practicar Ciclo for con Manipulación de Listas en Python

#1
print("Invertir una lista")
lista1=[1,2,3,4,5,6]
lista_invertida=[]
for i in range(len(lista1)-1,-1,-1):
    lista_invertida.append(lista1[i])
print("Lista invertida:", lista_invertida)

#2
print("Eliminar los números negativos")
numeros1=[3, -1, 5, -2, 7]
positivos = []
for numero in numeros1:
    if numero >= 0:
        positivos.append(numero)
print("Los números positivos son:",positivos)

#3
print("Encontrar la suma de los cuadrados")
numeros3=[1,2,3,4]
sumacuadrados3=0
for i in numeros3:
  sumacuadrados3+=i**2
print(sumacuadrados3)

#4
print("Duplicar los valores de una lista")
numeros4=[22,33,56,25,24]
nuevalista4=[]
for i in numeros4:
    nuevalista4.append(i*2)
print(nuevalista4)

#5
print("Contar elementos específicos")
numero_buscar = int(input("Ingresa el número que quieres contar: "))
entrada = input("Ingresa una lista de números separados por espacios: ")

lista = [int(x) for x in entrada.split()]
contador = 0

for numero in lista:
    if numero == numero_buscar:
        contador += 1

print(f"El número {numero_buscar} aparece {contador} veces en la lista.")

#6
print("Eliminar duplicados de una lista")
lista6=[1,1,1,2,6,5,5,7,7,8,2,4,4]
sinnumerosduplicados=[]
for x in lista6:
    if x not in sinnumerosduplicados:
        sinnumerosduplicados.append(x)
print(sinnumerosduplicados)

#7
print("Generar una lista de multiplos de un número")
numero7=int(input("Ingresa un número: "))
multiplos=[]
for i in range(1,11):
    multiplos.append(numero7*i)
print(multiplos)

#8
print("Sumar los elementos en las posiciones pares")
lista8=[11,12,13,14,15,16,17]
suma8=0
for j in range(0,len(lista8),2):
    suma8+=lista8[j]
print(f"La suma de los elementos en posiciones pares es: {suma8}")

#9
cadenas9=["fiesta", "globo", "piñata", "regalo","invitación","amistad"]
cadenaslargas=[]
for c in cadenas9:
    if len(c)>5:
        cadenaslargas.append(c)
print(f"Cadenas con más de 5 caracteres: {cadenaslargas}")

#10
lista10=[6,4,2,1,3,5]
for i in range(len(lista10)):
    for y in range(0,len(lista10)-i -1):
        if lista10[y]> lista10[y +1]:
            lista10[y], lista10[y+1]=lista10[y+1], lista10[y]
print(f"Lista ordenada de menor a mayor: {lista10}")