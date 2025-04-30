# ============================================
# Taller Investigativo: Arrays (Listas) en Python
# ============================================

# 1. ¿Qué es un array o lista en Python?
# R: En Python, una lista (también llamada array) es una estructura que almacena una secuencia de elementos.
#    Es ordenada, se puede modificar (es mutable) y puede contener cualquier tipo de dato.

# ¿Cómo se declara una lista vacía?
mi_lista_vacia = []

# ¿Cómo se crea una lista con valores iniciales?
mi_lista = [1, 2, 3, 4, 5]

# Ejemplo práctico:
print("Ejemplo práctico 1: Crear una lista con los números del 1 al 5")
print("mi_lista =", mi_lista)

# -----------------------------------------------------

# 2. ¿Cómo accedemos a los elementos de una lista?
# R: Para acceder usamos índices. El primer elemento está en la posición 0.
#    Los índices negativos acceden desde el final hacia atrás.
#    Si se usa un índice que no existe, se produce un error.

mi_lista2 = [10, 20, 30, 40]

# Ejemplo práctico:
print("\nEjemplo práctico 2: Acceder al primer y al último elemento")
print("Primer elemento:", mi_lista2[0])     # Índice 0
print("Último elemento (índice -1):", mi_lista2[-1])  # Índice negativo

# -----------------------------------------------------

# 3. ¿Qué es el 'slicing' o rebanado de listas?
# R: Es obtener una sublista usando rangos de índices: lista[inicio:fin].
#    Si se deja vacío el inicio, comienza desde el principio.
#    Si se deja vacío el fin, llega hasta el final.

mi_lista3 = [10, 20, 30, 40, 50]

# Ejemplo práctico:
print("\nEjemplo práctico 3: Usar slicing para obtener sublistas")
print("Índices del 1 al 3:", mi_lista3[1:4])
print("Primeros 3 elementos:", mi_lista3[:3])
print("Desde el índice 2 hasta el final:", mi_lista3[2:])

# -----------------------------------------------------

# 4. ¿Cómo modificamos los elementos de una lista?
# R: Se cambia escribiendo lista[posición] = nuevo_valor.
#    Si se usa un índice que no existe, da error.

mi_lista4 = [10, 20, 30, 40]
mi_lista4[2] = 99

# Ejemplo práctico:
print("\nEjemplo práctico 4: Cambiar el tercer elemento de la lista por 99")
print("Lista modificada:", mi_lista4)

# -----------------------------------------------------

# 5. ¿Cómo agregamos nuevos elementos a una lista?
# R:
#    .append() agrega al final.
#    .insert() agrega en una posición específica.
#    .extend() une listas.

mi_lista5 = [10, 20, 30]
mi_lista5.append(40)
mi_lista5.insert(1, 15)
mi_lista5.extend([50, 60])

# Ejemplo práctico:
print("\nEjemplo práctico 5: Agregar elementos a una lista")
print("Lista después de append, insert y extend:", mi_lista5)

# -----------------------------------------------------

# 6. ¿Cómo eliminamos elementos de una lista?
# R:
#    .remove(valor) elimina el primer valor que encuentra.
#    .pop() elimina el último por defecto o uno por índice.
#    del lista[posición] elimina por posición.

mi_lista6 = [10, 20, 30, 40, 50]
mi_lista6.remove(30)
mi_lista6.pop()
del mi_lista6[1]

# Ejemplo práctico:
print("\nEjemplo práctico 6: Eliminar elementos de una lista")
print("Lista después de remover 30, hacer pop y eliminar el índice 1:", mi_lista6)

# -----------------------------------------------------

# 7. ¿Cómo buscamos elementos dentro de una lista?
# R:
#    "in" verifica existencia.
#    .index(valor) da la posición.
#    .count(valor) cuenta cuántas veces aparece.

mi_lista7 = [10, 20, 30, 40, 50]

# Ejemplo práctico:
print("\nEjemplo práctico 7: Buscar elementos en una lista")
print("¿Está el 20 en la lista?", 20 in mi_lista7)
print("Índice del número 30:", mi_lista7.index(30))
print("Veces que aparece 20:", mi_lista7.count(20))

# -----------------------------------------------------

# 8. ¿Cómo ordenamos los elementos de una lista?
# R:
#    .sort() ordena la lista actual.
#    sorted() crea una nueva lista ordenada.

mi_lista8 = [40, 10, 30, 20]
lista_asc = sorted(mi_lista8)
mi_lista8.sort(reverse=True)

# Ejemplo práctico:
print("\nEjemplo práctico 8: Ordenar listas")
print("Lista ordenada ascendentemente con sorted():", lista_asc)
print("Lista ordenada descendente con sort(reverse=True):", mi_lista8)

# -----------------------------------------------------

# 9. ¿Cómo invertimos el orden de los elementos de una lista?
# R:
#    .reverse() invierte en el lugar.
#    lista[::-1] crea una nueva lista invertida.

mi_lista9 = [10, 20, 30, 40]
invertida1 = mi_lista9[::-1]
mi_lista9.reverse()

# Ejemplo práctico:
print("\nEjemplo práctico 9: Invertir el orden de una lista")
print("Invertida con reverse():", mi_lista9)
print("Invertida con slicing:", invertida1)

# -----------------------------------------------------

# 10. ¿Cómo hacemos una copia de una lista?
# R:
#    lista[:] crea una copia.
#    list(lista) también.
#    lista.copy() también.

mi_lista10 = [10, 20, 30]
copia1 = mi_lista10[:]
copia2 = list(mi_lista10)
copia3 = mi_lista10.copy()

# Ejemplo práctico:
print("\nEjemplo práctico 10: Copiar una lista")
print("Copia con slicing:", copia1)
print("Copia con list():", copia2)
print("Copia con copy():", copia3)

# -----------------------------------------------------

# 11. ¿Cómo comprobamos si una lista está vacía?
# R:
#    Si la lista está vacía, su valor es False al usarla en una condición.

mi_lista11 = []

# Ejemplo práctico:
print("\nEjemplo práctico 11: Verificar si una lista está vacía")
if not mi_lista11:
    print("La lista está vacía")
else:
    print("La lista tiene elementos")

# -----------------------------------------------------

# 12. ¿Cómo pedir varios datos al usuario y almacenarlos en una lista?
# R:
#    Se usa input() dentro de un ciclo for para pedir cada dato.
#    Se puede preguntar primero cuántos datos desea ingresar.

# Ejemplo práctico:
print("\nEjemplo práctico 12: Pedir datos al usuario y guardarlos en una lista")

cantidad = int(input("¿Cuántos elementos deseas ingresar?: "))
lista_usuario = []

for i in range(cantidad):
    dato = input(f"Ingresa el elemento #{i+1}: ")
    lista_usuario.append(dato)

print("Lista final con los datos del usuario:", lista_usuario)