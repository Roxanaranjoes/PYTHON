# 🔁 Estructuras de Control en Python

En este documento aprenderás a usar **estructuras de control** en Python: condicionales (`if`, `elif`, `else`) y bucles (`for`, `while`). También cubriremos los comandos `break` y `continue`, fundamentales para el control del flujo dentro de bucles.

---

## 📘 ¿Qué son las estructuras de control?

Son instrucciones que permiten **modificar el flujo de ejecución** de un programa dependiendo de condiciones o repeticiones. Con ellas, puedes tomar decisiones y repetir bloques de código.

---

## 🔷 Condicionales: `if`, `elif`, `else`

### 📌 `if`: evalúa si una condición es verdadera

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
```

### 📌 `elif`: se evalúa si la condición anterior fue falsa

```python
nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
```

### 📌 `else`: se ejecuta si todas las condiciones anteriores son falsas

```python
nota = 60

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

#### ✅ Ejercicio resuelto
```python
numero = int(input("Ingrese un número: "))

if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es cero")
```

---

## 🔁 Bucles

### 🔹 `for`: iteración sobre secuencias

```python
for i in range(5):
    print("Iteración:", i)
```

- `range(n)`: genera una secuencia desde `0` hasta `n-1`

### 🔹 `while`: se repite mientras la condición sea verdadera

```python
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
```

---

## 🔚 `break` y `continue`

### 🔸 `break`: termina el bucle actual inmediatamente

```python
for i in range(10):
    if i == 5:
        break
    print("Número:", i)
```

### 🔸 `continue`: salta la iteración actual y continúa con la siguiente

```python
for i in range(5):
    if i == 2:
        continue
    print("Valor:", i)
```

---

## 🧪 Ejercicios resueltos

### ✅ Suma de los primeros 10 números naturales
```python
suma = 0
for i in range(1, 11):
    suma += i
print("Suma:", suma)
```

### ✅ Contador con `while` y `break`
```python
contador = 0
while True:
    print("Contando:", contador)
    contador += 1
    if contador > 4:
        break
```

### ✅ Imprimir solo números impares con `continue`
```python
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print("Impar:", i)
```

---

## 💡 Buenas prácticas

- Evita bucles infinitos innecesarios (`while True`) sin condiciones de salida.
- Usa `break` y `continue` con moderación para mantener código legible.
- Usa `elif` en lugar de varios `if` independientes para mayor claridad.

---

## 📚 Recursos oficiales

- [Condicionales en Python - python.org](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Bucles en Python - python.org](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Instrucciones break y continue](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements)

---

## 🔐 Licencia

MIT License. Usa, comparte y modifica libremente.