
# Guía Completa sobre Validación de Errores y Resolución de Problemas en Python

Este archivo README es una guía exhaustiva sobre cómo manejar errores en Python, cómo abordar la resolución de problemas paso a paso, con ejemplos prácticos, ejercicios, tips, trucos y referencias a la documentación oficial de Python.

---

## 📌 Validación y Manejo de Errores en Python

Python proporciona un sistema robusto de manejo de errores basado en **excepciones**.

### 🔍 ¿Qué es una excepción?

Una **excepción** es un error que ocurre durante la ejecución del programa, que interrumpe el flujo normal.

### 🧱 Bloques try/except

```python
try:
    # Código que puede causar error
except TipoDeExcepcion:
    # Código que maneja el error
```

### Ejemplo básico:
```python
try:
    x = int(input("Ingrese un número: "))
except ValueError:
    print("Eso no es un número válido.")
```

### 🧰 Múltiples except:
```python
try:
    archivo = open("datos.txt")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
except IOError:
    print("Error de entrada/salida.")
```

### else y finally:
```python
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("No se puede dividir por cero.")
else:
    print("Todo salió bien:", resultado)
finally:
    print("Esto se ejecuta siempre.")
```

---

## ⚠️ Tipos Comunes de Excepciones

| Excepción            | Descripción                             |
|----------------------|-----------------------------------------|
| `ValueError`         | Tipo de dato incorrecto                 |
| `TypeError`          | Tipo de operación inválida              |
| `IndexError`         | Índice fuera de rango                   |
| `KeyError`           | Clave inexistente en diccionario        |
| `FileNotFoundError`  | Archivo no encontrado                   |
| `ZeroDivisionError`  | División por cero                       |
| `AttributeError`     | Atributo inexistente                    |

Ver más en la documentación oficial: https://docs.python.org/es/3/library/exceptions.html

---

## 🧠 Tips para Pensar y Resolver Problemas

### 1. Entender el problema
- ¿Qué se espera como entrada?
- ¿Qué se espera como salida?

### 2. Dividir en partes pequeñas
- Resolver subproblemas primero.
- Usar pseudocódigo o diagramas.

### 3. Probar con ejemplos simples
- Validar la lógica antes de complicar el caso.

### 4. Validación de entradas
- Verificar tipos, rangos, formato.

```python
def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos argumentos deben ser números")
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
```

### 5. Depurar
- Usar `print`, `logging`, o depuradores (pdb, IDEs).

---

## 🧪 Ejercicios

### Ejercicio 1: Validar entrada numérica
```python
def pedir_entero():
    while True:
        try:
            return int(input("Ingrese un número entero: "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
```

### Ejercicio 2: Leer archivo con manejo de errores
```python
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
```

### Ejercicio 3: Función robusta de división
```python
def dividir_seguro():
    try:
        a = float(input("Numerador: "))
        b = float(input("Denominador: "))
        print("Resultado:", a / b)
    except ValueError:
        print("Debe ingresar números.")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
```

---

## 🧙 Trucos y Buenas Prácticas

- Usa excepciones específicas, evita `except:` solo.
- Nunca ocultes errores sin loguearlos o tratarlos.
- Usa `raise` para relanzar errores si es necesario.
- Puedes definir tus propias excepciones:

```python
class ErrorPersonalizado(Exception):
    pass

raise ErrorPersonalizado("Este es un error definido por el usuario.")
```

- Usa `assert` para verificar condiciones durante el desarrollo:

```python
assert 2 + 2 == 4, "La suma no es correcta"
```

---

## 📚 Referencias Oficiales

- Manejo de excepciones: https://docs.python.org/es/3/tutorial/errors.html
- Tipos de excepciones: https://docs.python.org/es/3/library/exceptions.html
- Buenas prácticas: https://peps.python.org/pep-0008/#programming-recommendations

---

