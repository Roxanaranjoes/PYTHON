# 🐍 Operadores en Python

Este documento es una guía completa sobre los **operadores en Python**, diseñada especialmente para principiantes. Aprenderás qué son los operadores, los tipos que existen, cómo usarlos con ejemplos y ejercicios resueltos. También incluye enlaces a documentación oficial para profundizar.

---

## 📘 ¿Qué es un operador?

Un operador es un símbolo que le dice al intérprete de Python que realice una operación matemática, lógica o de comparación entre valores u objetos.

---

## 🔢 Tipos de Operadores en Python

### 1. Operadores Aritméticos

| Operador | Descripción           | Ejemplo `a = 10`, `b = 3` | Resultado |
|----------|------------------------|---------------------------|-----------|
| `+`      | Suma                   | `a + b`                   | `13`      |
| `-`      | Resta                  | `a - b`                   | `7`       |
| `*`      | Multiplicación         | `a * b`                   | `30`      |
| `/`      | División               | `a / b`                   | `3.3333`  |
| `//`     | División entera        | `a // b`                  | `3`       |
| `%`      | Módulo (residuo)       | `a % b`                   | `1`       |
| `**`     | Exponenciación         | `a ** b`                  | `1000`    |

#### ✅ Ejercicio resuelto:
```python
def operaciones_basicas(a, b):
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicación:", a * b)
    print("División:", a / b)
    print("Residuo:", a % b)

operaciones_basicas(10, 3)
```

---

### 2. Operadores de Asignación

```python
x = 10
print("Inicial:", x)

x += 5
print("Suma acumulada:", x)

x *= 2
print("Multiplicado por 2:", x)

x //= 3
print("División entera entre 3:", x)
```

#### ✅ Ejercicio resuelto:
```python
contador = 0
while contador < 100:
    contador += 10
    print("Contador:", contador)
```

---

### 3. Operadores de Comparación

| Operador | Ejemplo | Resultado |
|----------|---------|-----------|
| `==`     | `5 == 5`| `True`    |
| `!=`     | `5 != 3`| `True`    |
| `>`      | `5 > 3` | `True`    |
| `<`      | `5 < 3` | `False`   |
| `>=`     | `5 >= 5`| `True`    |
| `<=`     | `5 <= 4`| `False`   |

#### ✅ Ejercicio resuelto:
```python
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a > b:
    print("El primer número es mayor.")
elif a < b:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")
```

---

### 4. Operadores Lógicos

```python
edad = 20
es_colombiano = True

if edad >= 18 and es_colombiano:
    print("Puede votar.")
else:
    print("No puede votar.")
```

#### ✅ Ejercicio resuelto:
```python
edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ").lower()

if edad >= 18 and nacionalidad == "colombiana":
    print("Puede votar.")
else:
    print("No puede votar.")
```

---

### 5. Operadores de Identidad

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)     # True
print(x is z)     # False
print(x == z)     # True (comparación de contenido)
```

---

### 6. Operadores de Pertenencia

```python
fruta = "manzana"
print("a" in fruta)     # True
print("z" not in fruta) # True
```

---

### 7. Operadores Bit a Bit (Bitwise)

```python
a = 5       # binario: 0101
b = 3       # binario: 0011

print("AND:", a & b)       # 1
print("OR:", a | b)        # 7
print("XOR:", a ^ b)       # 6
print("NOT:", ~a)          # -6
print("Izquierda:", a << 1)# 10
print("Derecha:", a >> 1)  # 2
```

#### ✅ Ejercicio resuelto:
```python
# Verificar si un número es par usando bitwise
numero = int(input("Ingrese un número: "))

if numero & 1 == 0:
    print("Es par.")
else:
    print("Es impar.")
```

---

## 🧠 Ejercicio general resuelto

```python
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

# Comparación
if a == b:
    print("Los números son iguales.")
elif a > b:
    print("El primer número es mayor.")
else:
    print("El segundo número es mayor.")

# Operaciones
print("Suma:", a + b)
print("Diferencia:", a - b)
print("Producto:", a * b)
print("Cociente:", a / b if b != 0 else "División por cero")

# Condiciones
print("Ambos mayores a 10:", a > 10 and b > 10)
print("Al menos uno entre 5 y 15:", (5 <= a <= 15) or (5 <= b <= 15))
```

---

## 📚 Recursos oficiales

- [📖 Documentación oficial de operadores en Python (python.org)](https://docs.python.org/3/reference/expressions.html#operator-summary)
- [👩‍💻 Tutorial oficial de Python](https://docs.python.org/3/tutorial/)
- [🧮 Bitwise Operations](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)

---

## 🧾 Contribuciones

¿Quieres mejorar este documento? Haz un fork o pull request.

---

## 🔐 Licencia

MIT License. Usa, comparte y modifica libremente.