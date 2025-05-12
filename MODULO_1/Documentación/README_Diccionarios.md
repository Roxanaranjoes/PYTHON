# 📘 Todo sobre Diccionarios en Python

Los **diccionarios** en Python son colecciones no ordenadas y mutables de pares clave-valor. Son una estructura muy útil para representar datos asociados.

---

## 🧱 ¿Qué es un diccionario?

Un diccionario está formado por **claves** únicas y sus valores asociados.

```python
mi_diccionario = {"nombre": "Juan", "edad": 30, "activo": True}
```

---

## 🔧 Crear diccionarios

```python
vacio = {}
persona = dict(nombre="Ana", edad=25)
```

---

## 🧪 Acceder a elementos

```python
persona = {"nombre": "Ana", "edad": 25}
print(persona["nombre"])  # Ana
print(persona.get("edad"))  # 25
```

### Con `get()` evitas errores si la clave no existe:

```python
print(persona.get("ciudad", "No disponible"))  # No disponible
```

---

## 📝 Agregar o modificar valores

```python
persona["ciudad"] = "Lima"  # Agregar
persona["edad"] = 26        # Modificar
```

---

## ❌ Eliminar elementos

```python
del persona["edad"]
persona.pop("nombre")
persona.clear()  # Borra todo el diccionario
```

---

## 🔁 Recorrer un diccionario

```python
for clave in persona:
    print(clave, ":", persona[clave])
```

```python
for clave, valor in persona.items():
    print(clave, "->", valor)
```

---

## 🧰 Métodos útiles

| Método             | Descripción                                     |
|-------------------|-------------------------------------------------|
| `get(clave)`      | Devuelve el valor de una clave                  |
| `keys()`          | Devuelve todas las claves                       |
| `values()`        | Devuelve todos los valores                      |
| `items()`         | Devuelve tuplas (clave, valor)                  |
| `pop(clave)`      | Elimina una clave y devuelve su valor           |
| `popitem()`       | Elimina el último par agregado                  |
| `update(dict2)`   | Agrega pares de otro diccionario                |
| `clear()`         | Elimina todos los elementos                     |
| `copy()`          | Retorna una copia superficial del diccionario  |

---

## ✅ Ejercicios resueltos

### 1. Crear un diccionario con 3 contactos y sus teléfonos

```python
contactos = {"Ana": "1234", "Luis": "5678", "Marta": "9101"}
print(contactos)
```

### 2. Mostrar solo las claves

```python
for nombre in contactos.keys():
    print(nombre)
```

### 3. Mostrar solo los valores

```python
for telefono in contactos.values():
    print(telefono)
```

### 4. Buscar un teléfono y mostrar un mensaje si no existe

```python
nombre = "Carlos"
print(contactos.get(nombre, "Contacto no encontrado"))
```

### 5. Contar cuántas veces aparece cada letra en una frase

```python
frase = "python es genial"
contador = {}
for letra in frase:
    if letra != " ":
        contador[letra] = contador.get(letra, 0) + 1
print(contador)
```

---

## 💡 Trucos y consejos

- Usar `dict()` para crear rápidamente: `dict(nombre="Ana", edad=30)`
- Puedes combinar listas en un diccionario:  
  ```python
  claves = ["a", "b"]
  valores = [1, 2]
  dic = dict(zip(claves, valores))
  ```
- Usar comprensión de diccionario:  
  ```python
  cuadrados = {x: x**2 for x in range(5)}
  ```

---

## 🧭 Orden en diccionarios

Desde Python 3.7, los diccionarios **mantienen el orden** de inserción de los elementos.

---

## 📚 Recursos oficiales

- [Tutorial oficial de Python - Diccionarios](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Referencia de tipos - dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

---

## 🔐 Licencia

MIT License. Puedes usar, copiar y modificar libremente.