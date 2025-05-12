# Bucle `for` en Python

El bucle `for` en Python se utiliza para iterar sobre los elementos de una secuencia como listas, tuplas, diccionarios, conjuntos y cadenas. Es una de las estructuras de control más comunes.

---

## Sintaxis

```python
for variable in secuencia:
    # Bloque de código
```

---

## Ejemplos básicos

### Iterar sobre una lista
```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```

### Iterar sobre una cadena
```python
for letra in "Python":
    print(letra)
```

### Uso de `range()`
```python
for i in range(5):
    print(i)
```

### Uso de `range()` con inicio, fin y paso
```python
for i in range(2, 10, 2):
    print(i)
```

---

## Funciones útiles con `for`

### `len()` para recorrer con índices
```python
nombres = ["Ana", "Luis", "Carlos"]
for i in range(len(nombres)):
    print(f"Índice {i}: {nombres[i]}")
```

### `enumerate()`
```python
for i, nombre in enumerate(nombres):
    print(i, nombre)
```

### `zip()`
```python
nombres = ["Ana", "Luis", "Carlos"]
edades = [20, 21, 19]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```

### Emojis
```python
emojis = ["🐱", "🐶", "🐟"]
nombres = ["gato", "perro", "pez"]
for i in range(len(emojis)):
    print(f"{emojis[i]} {nombres[i]}")
```

---

## Ejercicios prácticos

### 1. Sumar todos los números del 1 al 100
```python
suma = 0
for i in range(1, 101):
    suma += i
print(suma)
```

### 2. Imprimir solo números pares entre 1 y 50
```python
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
```

### 3. Contar vocales en una palabra
```python
palabra = "murciélago"
vocales = "aeiouáéíóú"
contador = 0
for letra in palabra.lower():
    if letra in vocales:
        contador += 1
print(f"Vocales: {contador}")
```

### 4. Multiplicar elementos de una lista
```python
numeros = [1, 2, 3, 4]
resultado = 1
for numero in numeros:
    resultado *= numero
print(resultado)
```

### 5. Crear una nueva lista con cuadrados de los números del 1 al 10
```python
cuadrados = []
for i in range(1, 11):
    cuadrados.append(i ** 2)
print(cuadrados)
```

---

## Recursos y documentación oficial

- [Control de flujo en Python (for)](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Funciones integradas como `range()`](https://docs.python.org/3/library/functions.html#func-range)
- [Función `len()`](https://docs.python.org/3/library/functions.html#len)
- [Función `enumerate()`](https://docs.python.org/3/library/functions.html#enumerate)
- [Función `zip()`](https://docs.python.org/3/library/functions.html#zip)

---

Este documento ofrece una guía práctica y clara sobre el uso del bucle `for` en Python, ideal para estudiantes, autodidactas y profesionales en formación.