# 🐍 Introducción a Python

Bienvenido a esta guía básica sobre Python. Este archivo está diseñado para ayudarte a comenzar con uno de los lenguajes de programación más populares, versátiles y amigables del mundo.

---

## 📌 ¿Qué es Python?

Python es un lenguaje de programación de alto nivel, interpretado, de propósito general. Fue creado por **Guido van Rossum** y lanzado en 1991. Es conocido por su sintaxis sencilla y legible.

---

## 🎯 Características de Python

- **Sintaxis clara y legible**
- **Multiparadigma**: soporta programación orientada a objetos, funcional e imperativa
- **Gran comunidad y bibliotecas**
- **Portabilidad**: corre en múltiples plataformas
- **Ideal para principiantes**

---

## 🛠 Instalación

### Windows/macOS/Linux

1. Visita [python.org](https://www.python.org/downloads/)
2. Descarga el instalador para tu sistema operativo
3. Ejecuta el instalador y asegúrate de marcar “Add Python to PATH”

Para verificar si está instalado:
```bash
python --version
```

---

## ✍️ Tu primer programa

Crea un archivo `hola.py` con el siguiente contenido:

```python
print("¡Hola, mundo!")
```

Ejecuta desde terminal:
```bash
python hola.py
```

---

## 🧠 Conceptos básicos

### 1. Variables y tipos de datos

```python
nombre = "Juan"
edad = 30
altura = 1.75
es_estudiante = True
```

### 2. Entradas y salidas

```python
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
```

### 3. Condicionales

```python
edad = int(input("¿Cuántos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

### 4. Bucles

```python
for i in range(5):
    print("Repetición", i)

contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
```

### 5. Funciones

```python
def saludar(nombre):
    print("Hola,", nombre)

saludar("Ana")
```

---

## 🧪 Ejercicios resueltos

### ✅ Calcular el área de un triángulo

```python
base = float(input("Base: "))
altura = float(input("Altura: "))
area = (base * altura) / 2
print("Área:", area)
```

### ✅ Conversor de grados Celsius a Fahrenheit

```python
celsius = float(input("Temperatura en °C: "))
fahrenheit = (celsius * 9/5) + 32
print("Equivalente en °F:", fahrenheit)
```

---

## 📚 Recursos adicionales

- [Documentación oficial de Python](https://docs.python.org/3/)
- [Curso gratuito en Python.org](https://docs.python.org/3/tutorial/index.html)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

---

## 🔐 Licencia

MIT License. Usa, comparte y modifica libremente.