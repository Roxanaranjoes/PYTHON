# 📚 Todo sobre Listas en Python

Las **listas** en Python son estructuras de datos que permiten almacenar múltiples elementos en un solo objeto. Son muy versátiles y se usan ampliamente.

---

## 🧱 ¿Qué es una lista?

Una lista es una colección **ordenada** y **mutable** de elementos, que pueden ser de diferentes tipos.

```python
mi_lista = [1, 2, 3, "Python", True]
```

---

## 🔧 Crear listas

```python
vacia = []
numeros = [1, 2, 3]
mixta = [1, "texto", False, 3.14]
```

---

## 🧪 Acceder a elementos

```python
numeros = [10, 20, 30]
print(numeros[0])  # 10
print(numeros[-1])  # 30 (último elemento)
```

---

## 🔁 Recorrer una lista

```python
for item in numeros:
    print(item)
```

---

## 🧰 Métodos comunes de listas

| Método            | Descripción                              | Ejemplo                             |
|------------------|------------------------------------------|-------------------------------------|
| `append()`       | Agrega un elemento al final               | `lista.append(5)`                   |
| `insert()`       | Inserta un elemento en un índice          | `lista.insert(1, "Hola")`           |
| `remove()`       | Elimina la primera aparición de un valor  | `lista.remove("Hola")`              |
| `pop()`          | Elimina y devuelve un elemento            | `lista.pop()`                       |
| `clear()`        | Elimina todos los elementos               | `lista.clear()`                     |
| `index()`        | Devuelve índice de la primera coincidencia| `lista.index("Python")`             |
| `count()`        | Cuenta ocurrencias de un elemento         | `lista.count(3)`                    |
| `sort()`         | Ordena la lista                           | `lista.sort()`                      |
| `reverse()`      | Invierte el orden                         | `lista.reverse()`                   |
| `copy()`         | Devuelve una copia de la lista            | `nueva = lista.copy()`              |

---

## 🧪 Comprobación de pertenencia

```python
if "Python" in mi_lista:
    print("¡Encontrado!")
```

---

## ✂️ Slicing (rebanado de listas)

```python
lista = [0, 1, 2, 3, 4, 5]
print(lista[1:4])  # [1, 2, 3]
print(lista[:3])   # [0, 1, 2]
print(lista[::2])  # [0, 2, 4]
```

---

## 🔄 Listas por comprensión (List Comprehension)

```python
cuadrados = [x**2 for x in range(6)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25]
```

---

## ✅ Ejercicios resueltos

### 1. Sumar todos los elementos de una lista

```python
numeros = [1, 2, 3, 4]
suma = sum(numeros)
print("Suma:", suma)
```

### 2. Obtener los números pares de una lista

```python
numeros = [1, 2, 3, 4, 5, 6]
pares = [n for n in numeros if n % 2 == 0]
print(pares)
```

### 3. Eliminar duplicados de una lista

```python
lista = [1, 2, 2, 3, 4, 4]
sin_duplicados = list(set(lista))
print(sin_duplicados)
```

### 4. Invertir una lista

```python
lista = [1, 2, 3]
lista.reverse()
print(lista)
```

### 5. Concatenar listas

```python
a = [1, 2]
b = [3, 4]
c = a + b
print(c)
```

---

## 💡 Trucos y consejos

- Puedes usar `*` para repetir listas: `[1, 2] * 3 → [1, 2, 1, 2, 1, 2]`
- Para evitar modificar la original al copiar: `lista2 = lista1.copy()` o `lista2 = lista1[:]`
- Para iterar con índices: `for i, valor in enumerate(lista): ...`
- Ordenar sin modificar: `sorted(lista)`
- Combinar listas con `zip`: `for a, b in zip(lista1, lista2): ...`

---

## 📚 Recursos oficiales

- [Tutorial oficial de Python - Listas](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Referencia de métodos de lista](https://docs.python.org/3/library/stdtypes.html#list)

---

## 🔐 Licencia

MIT License. Puedes usar, copiar y modificar libremente.