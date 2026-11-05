"""
Actividad 38 - Inventario con diccionario anidado
Representa un pequeño inventario como un diccionario donde cada clave es un producto y
su valor es otro diccionario con “precio” y “stock”. Escribe una función que calcule el valor
total del inventario (precio × stock de cada producto, sumado)
"""
def calcular_inventario(inventario):
    # Recorremos el parametro que nos pasan (la lista de productos), no una
    # variable de fuera, para que la funcion serve con cualquier inventario
    total_inventario = 0
    for elemento in inventario:
        producto = elemento["producto"]
        print(f"Nombre : {producto['nombre']} | Precio: {producto['precio']} | Stock: {producto['stock']}")
        # Cada producto vale su precio multiplicado por las unidades en stock
        total_inventario += producto["precio"] * producto["stock"]

    print(f"El valor total del inventario es: {total_inventario}")

lista_productos = []

entrada_usuario = ""

# El bucle pide productos hasta que el usuario escriba "fin". La variable
# entrada_usuario se inicializa a "" (distinta de "fin") para que la primera
# vuelta se ejecute siempre
while entrada_usuario != "fin":
    entrada_usuario = input("Introduce el nombre del producto (o 'fin' para terminar): ")

    # Con break salimos del bucle sin guardar "fin" como si fuera un producto
    if entrada_usuario == "fin":
        break
    else:
        nombre_producto = entrada_usuario
        precio_producto = float(input("Introduce el precio del producto: "))
        stock_producto = int(input("Introduce el stock del producto: "))

        # Diccionario con los datos del producto
        producto = {
            "nombre" : nombre_producto,
            "precio" : precio_producto,
            "stock" : stock_producto
        }

        # Y otro diccionario que lo envuelve, para tener el inventario anidado
        inventario = {
            "producto" : producto
        }

        # Cada producto se guarda como un elemento mas de la lista
        lista_productos.append(inventario)


calcular_inventario(lista_productos)
