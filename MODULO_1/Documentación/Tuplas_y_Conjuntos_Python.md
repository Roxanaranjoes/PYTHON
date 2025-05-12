
# Guía Completa sobre Tuplas y Conjuntos en Python

Este archivo README proporciona una guía detallada sobre el uso de **tuplas** y **conjuntos** en Python, con ejemplos, ejercicios prácticos, trucos útiles y referencias a la documentación oficial.

---

## 📌 Tuplas en Python

Una **tupla** es una estructura de datos inmutable, ordenada, y que puede contener elementos heterogéneos.

### Sintaxis:
```python
mi_tupla = (1, 2, 3)
otra_tupla = "a", "b", "c"
tupla_unitaria = (5,)
```

### Características:
- Inmutables (no se pueden modificar).
- Permiten elementos duplicados.
- Se pueden anidar.

### Métodos útiles:
```python
mi_tupla.count(2)  # Cuenta cuántas veces aparece el 2
mi_tupla.index(3)  # Devuelve el índice del valor 3
```

### Trucos:
- Para desempaquetar:
```python
a, b, c = mi_tupla
```

- Desempaquetado extendido:
```python
a, *resto = (1, 2, 3, 4)
```

### Ejercicio:
```python
# Crear una tupla con 5 elementos y mostrar el tercero
tupla = (10, 20, 30, 40, 50)
print(tupla[2])  # Resultado esperado: 30
```

---

## 📌 Conjuntos en Python

Un **conjunto** es una colección desordenada de elementos únicos.

### Sintaxis:
```python
mi_conjunto = {1, 2, 3}
conjunto_vacio = set()
```

### Características:
- No permiten elementos duplicados.
- Son mutables.
- No garantizan orden.

### Métodos útiles:
```python
mi_conjunto.add(4)
mi_conjunto.remove(2)
mi_conjunto.discard(5)  # No lanza error si el elemento no existe
mi_conjunto.pop()
mi_conjunto.clear()
```

### Operaciones:
```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Unión
print(a & b)  # Intersección
print(a - b)  # Diferencia
print(a ^ b)  # Diferencia simétrica
```

### Trucos:
- Para eliminar duplicados de una lista:
```python
lista = [1, 2, 2, 3, 4, 4]
lista_sin_duplicados = list(set(lista))
```

### Ejercicio:
```python
# Crea un conjunto con los números del 1 al 5 y elimina el 3
conjunto = {1, 2, 3, 4, 5}
conjunto.remove(3)
print(conjunto)  # Resultado esperado: {1, 2, 4, 5}
```

---

## 📚 Referencias oficiales:

- Tuplas: https://docs.python.org/es/3/library/stdtypes.html#tuple
- Conjuntos: https://docs.python.org/es/3/library/stdtypes.html#set

---


