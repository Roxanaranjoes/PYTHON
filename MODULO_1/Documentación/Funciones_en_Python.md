
# Guía Completa sobre Funciones en Python

Este archivo README proporciona una guía detallada sobre el uso de **funciones** en Python, incluyendo funciones definidas por el usuario, funciones lambda, argumentos especiales, trucos, ejemplos prácticos y ejercicios con soluciones.

---

## 📌 ¿Qué es una función?

Una **función** es un bloque de código reutilizable que realiza una tarea específica. Se define con la palabra clave `def`.

### Sintaxis:
```python
def nombre_funcion(parámetros):
    """Docstring opcional"""
    # Cuerpo de la función
    return resultado
```

---

## 🧠 Tipos de funciones

### 1. Funciones definidas por el usuario
```python
def saludar(nombre):
    return f"Hola, {nombre}!"
```

### 2. Funciones con parámetros opcionales
```python
def potencia(base, exponente=2):
    return base ** exponente
```

### 3. Funciones con número variable de argumentos
```python
def sumar_todo(*args):
    return sum(args)

def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
```

---

## ⚡ Funciones Lambda (anónimas)

Una **lambda** es una función pequeña y anónima, útil para operaciones simples.

### Sintaxis:
```python
lambda argumentos: expresión
```

### Ejemplo:
```python
doble = lambda x: x * 2
print(doble(4))  # 8
```

### Uso común con `map`, `filter` y `sorted`:
```python
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
ordenado = sorted(["casa", "árbol", "sol"], key=lambda x: len(x))
```

---

## 🔍 Trucos y buenas prácticas

- Utiliza **docstrings** para documentar funciones:
```python
def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b
```

- Retorna múltiples valores como tuplas:
```python
def operaciones(a, b):
    return a + b, a - b, a * b, a / b
```

- Usa funciones como objetos:
```python
def aplicar_funcion(f, valor):
    return f(valor)

print(aplicar_funcion(lambda x: x * 10, 5))  # 50
```

---

## 🧪 Ejercicios

### Ejercicio 1:
```python
# Define una función que calcule el factorial de un número.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Ejercicio 2:
```python
# Usar una función lambda para elevar al cubo una lista de números.
numeros = [1, 2, 3, 4]
cubos = list(map(lambda x: x**3, numeros))
print(cubos)  # [1, 8, 27, 64]
```

### Ejercicio 3:
```python
# Crear una función que reciba una lista y una función, y devuelva una nueva lista transformada.
def transformar_lista(lista, funcion):
    return [funcion(x) for x in lista]

print(transformar_lista([1, 2, 3], lambda x: x + 5))  # [6, 7, 8]
```

---

## 📚 Referencias oficiales:

- Funciones: https://docs.python.org/es/3/tutorial/controlflow.html#defining-functions
- Funciones lambda: https://docs.python.org/es/3/reference/expressions.html#lambda

---


