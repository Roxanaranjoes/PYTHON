# Programa para calcular el costo total de una compra con descuento
print("Bienvenido al sistema de validación de productos\n")
#Solicitar nombre del producto
nombre_producto = input("Ingrese el nombre del producto: ")
while nombre_producto == "":
    print("El nombre no puede estar vacío.")
    nombre_producto = input("Ingrese el nombre del producto: ")
#Solicitar precio unitario
while True:
    try:
        precio_unitario = float(input("Ingrese el precio unitario del producto: "))
        if precio_unitario > 0:break
        else:print("El precio debe ser mayor que cero.")
    except ValueError:print("Error: debe ingresar un número válido.")
#Solicitar cantidad de productos
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de productos: "))
        if cantidad > 0:break
        else:print("La cantidad debe ser mayor que cero.")
    except ValueError:print("Error: debe ingresar un número entero.")
#Solicitar porcentaje de descuento
while True:
    try:
        descuento = float(input("Ingrese el porcentaje de descuento (0-100): "))
        if descuento >= 0 and descuento <= 100: break
        else:print("El descuento debe estar entre 0 y 100.")
    except ValueError:print("Error: debe ingresar un número válido.")
#Calcular costo total
costo_sin_descuento = precio_unitario * cantidad
monto_descuento = costo_sin_descuento * (descuento / 100)
costo_final = costo_sin_descuento - monto_descuento
#Mostrar Resultados
print("\nResumen de compra:");print("Producto:", nombre_producto);print("Cantidad:", cantidad)
print("Precio unitario: $", round(precio_unitario, 2));print("Descuento aplicado:", descuento, "%");print("Costo total: $", round(costo_final, 2))

