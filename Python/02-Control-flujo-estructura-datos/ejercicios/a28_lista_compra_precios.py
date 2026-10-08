"""
Actividad 28 - Lista de la compra con precios
Crea una lista vacía de tuplas (producto, precio). En un bucle, pide al usuario producto y
precio hasta que escriba “fin” como producto, y al terminar calcula con un bucle el importe
total a pagar
"""
# Cada elemento de esta lista sera una tupla con el nombre y el precio
lista_productos = []

entrada_usuario = ""

while entrada_usuario != "fin":
    entrada_usuario = input("Ingrese el nombre del producto: ")

    # Aqui el break si hace falta: en cuanto el usuario escribe "fin" salimos
    # del bucle y la palabra "fin" NO llega a guardarse como producto
    if entrada_usuario == "fin":
        break
    else:
        nombre_producto = entrada_usuario
        precio_producto = float(input("Ingrese el precio del producto: "))

        # Los parentesis crean la tupla (producto, precio) y append() la anade
        lista_productos.append((nombre_producto, precio_producto))

# Recorremos la lista sumando los precios. En una tupla se accede a cada valor
# por su posicion: producto[0] es el nombre y producto[1] el precio
importe = 0
for producto in lista_productos:
    importe += producto[1]

print(f"Importe total: {importe}")