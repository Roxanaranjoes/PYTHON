# Bucle `while` en Python

El bucle `while` en Python se ejecuta mientras una condición especificada sea verdadera. Se utiliza para repetir bloques de código sin saber cuántas veces se repetirá exactamente, lo que lo hace ideal para condiciones abiertas.

---

## Sintaxis

```python
while condición:
    # Bloque de código
```

---

## Ejemplos básicos

### Contador simple
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### Uso con condición booleana
```python
activo = True
while activo:
    entrada = input("Escribe 'salir' para terminar: ")
    if entrada == "salir":
        activo = False
```

---

## Control del flujo dentro del bucle

### `break`
```python
i = 0
while True:
    print(i)
    i += 1
    if i == 3:
        break
```

### `continue`
```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

---

## Ejercicios prácticos

### 1. Imprimir los números del 1 al 10
```python
n = 1
while n <= 10:
    print(n)
    n += 1
```

### 2. Sumar los primeros 100 números naturales
```python
suma = 0
n = 1
while n <= 100:
    suma += n
    n += 1
print(suma)
```

### 3. Adivina el número (juego)
```python
import random
secreto = random.randint(1, 10)
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (1-10): "))
    if intento == secreto:
        print("¡Correcto!")
        adivinado = True
    else:
        print("Intenta de nuevo.")
```

### 4. Contar vocales en una palabra
```python
palabra = "murciélago"
vocales = "aeiouáéíóú"
i = 0
contador = 0
while i < len(palabra):
    if palabra[i].lower() in vocales:
        contador += 1
    i += 1
print(f"Cantidad de vocales: {contador}")
```

### 5. Calcular factorial de un número
```python
numero = 5
resultado = 1
while numero > 1:
    resultado *= numero
    numero -= 1
print(resultado)
```

---

## Recursos y documentación oficial

- [Control de flujo en Python (while)](https://docs.python.org/3/tutorial/controlflow.html#the-while-statement)
- [Funciones integradas](https://docs.python.org/3/library/functions.html)

---

Este documento ofrece una guía práctica y clara sobre el uso del bucle `while` en Python, ideal para principiantes, estudiantes y desarrolladores que deseen reforzar su lógica de programación.