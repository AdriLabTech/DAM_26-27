"""
Actividad 33 - Ficha de producto
Crea un diccionario para representar un producto de una tienda, con las claves "nombre",
"precio" y "stock". Pide estos tres datos al usuario y guárdalos en el diccionario. Muestra
la ficha completa del producto con una f-string y, después, modifica el "stock" restando 1
unidad (simulando una venta) y muestra el diccionario actualizado.
"""
nombre_producto = input("Introduce el nombre del producto: ")
precio_producto = input("Introduce el precio del producto: ")
stock_producto = int(input("Introduce el stock actual del producto: "))

# Los datos del usuario se guardan en un diccionario con las tres claves del
# enunciado. El stock se convierte a int para poder hacer cuentas con el
producto = {
    "nombre": nombre_producto,
    "precio": precio_producto,
    "stock": stock_producto
}

# Muestra de la ficha. Dentro de la f-string se accede a cada dato escribiendo
# el diccionario y la clave entre corchetes
print("Producto: FICHA TECNICA")
print(f"Nombre del producto: {producto['nombre']}")
print(f"Precio del producto: {producto['precio']}")
print(f"Stock del producto: {producto['stock']}")

# Simulamos una venta: los diccionarios son mutables, asi que podemos cambiar el
# valor de una clave directamente con producto["stock"] -= 1
producto["stock"] -= 1

# Volvemos a mostrar la ficha para ver el stock ya descontado
print("Producto: FICHA TECNICA")
print(f"Nombre del producto: {producto['nombre']}")
print(f"Precio del producto: {producto['precio']}")
print(f"Stock del producto: {producto['stock']}")