"""
Actividad 30 — Excepción StockInsuficienteError. (Obligatoria) Crea una excepción
personalizada StockInsuficienteError (que herede de Exception). Guarda un pequeño
inventario en un archivo (producto,cantidad) y, al intentar vender más unidades de las
disponibles, lanza esa excepción y captúrala en el programa principal con un mensaje
claro.
"""
fichero = "../output/a30_inventario.txt"

# Nuestro propio tipo de error: "Exception" es la base de todos los errores normales
class StockInsuficienteError(Exception):
    pass

# Guarda el inventario (un diccionario) en el fichero, una linea por producto
def guardar_inventario(inventario):
    with open(fichero, "w", encoding="utf-8") as f:
        for producto, cantidad in inventario.items():
            f.write(f"{producto},{cantidad}\n")

# Lee el fichero y lo convierte otra vez en diccionario {producto: cantidad}
def leer_inventario():
    inventario = {}
    with open(fichero, "r", encoding="utf-8") as f:
        for linea in f:
            producto, cantidad = linea.strip().split(",")
            inventario[producto] = int(cantidad)
    return inventario

# Resta unidades al producto; si no hay suficientes, lanza nuestro error
def vender(inventario, producto, cantidad):
    if cantidad > inventario[producto]:
        raise StockInsuficienteError(
            f"solo quedan {inventario[producto]} de '{producto}' y se piden {cantidad}")
    inventario[producto] -= cantidad

# Creamos el inventario inicial y lo volvemos a leer desde el fichero
guardar_inventario({"manzanas": 10, "peras": 4, "kiwis": 0})
inventario = leer_inventario()
print(f"Inventario inicial: {inventario}")

for producto, cantidad in [("manzanas", 3), ("peras", 10), ("kiwis", 1), ("fresas", 1)]:
    try:
        vender(inventario, producto, cantidad)
        print(f"Vendidas {cantidad} de {producto}")
    except StockInsuficienteError as e:
        print(f"[VENTA CANCELADA]: {e}")
    except KeyError:
        print(f"[ERROR]: el producto {producto!r} no existe")

# Guardamos el inventario ya actualizado
guardar_inventario(inventario)
print(f"Inventario final: {leer_inventario()}")
