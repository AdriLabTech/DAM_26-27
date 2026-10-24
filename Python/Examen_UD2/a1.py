"""
El almacén es un diccionario cuyas claves son los nombres de los pasillos y 
cuyos valores son, a su vez, diccionarios {producto: unidades}. Un mismo 
producto puede estar en varios pasillos.
Crea el diccionario almacen con al menos [Y] pasillos (sustituye [Y] por 
la suma de los dos últimos dígitos de tu DNI/NIF; si sale menos de 3 usa 3 
y si sale más de 6 usa 6), cada uno con al menos dos productos. Al menos dos 
productos deben aparecer en más de un pasillo.
Escribe una función stock_total(almacen, producto) que devuelva las unidades 
de ese producto sumando todos los pasillos (0 si no existe en ninguno).
Escribe una función productos_criticos(almacen, minimo=20) que devuelva 
una lista, sin repetidos, con los productos cuyo stock total en todo el 
almacén sea menor que minimo.
Escribe una función reponer(almacen, pasillo, producto, minimo, 
lote=12, max_lotes=5) que, con un bucle while, añada lotes de lote unidades 
al producto en ese pasillo (que existe) mientras tenga menos de minimo unidades 
(si el producto no está en el pasillo, parte de 0). El bucle se detiene con break 
al llegar a max_lotes lotes. Devuelve el número de lotes añadidos.
Muestra stock_total de un producto repetido y de uno inexistente, productos_criticos 
con el valor por defecto y con minimo igual a 50, y el resultado de 
reponer un producto que ya existe en un pasillo y otro que no existe en él, 
comprobando después el nuevo stock.

"""
NUM_PASILLOS = 4

almacen = {
    "pasillo1": {"tornillos": 40, "clavos": 15, "tuercas": 8},
    "pasillo2": {"tornillos": 10, "pilas": 12, "cable": 30},
    "pasillo3": {"cable": 5, "pilas": 6, "bombillas": 25},
    "pasillo4": {"bombillas": 3, "martillos": 9, "clavos": 4},
}


def stock_total(almacen, producto):
    # Unidades del producto sumando todos los pasillos (0 si no existe)
    return sum(productos.get(producto, 0) for productos in almacen.values())


def productos_criticos(almacen, minimo=20):
    # Productos, sin repetidos, con stock total menor que minimo
    todos = {p for productos in almacen.values() for p in productos}
    return sorted(p for p in todos if stock_total(almacen, p) < minimo)


def reponer(almacen, pasillo, producto, minimo, lote=12, max_lotes=5):
    """
    Añade lotes al producto en el pasillo mientras tenga menos de minimo.
    Si el producto no está en el pasillo parte de 0. Devuelve los lotes añadidos.
    """
    productos = almacen[pasillo]
    productos[producto] = 0
    lotes = 0
    while productos[producto] < minimo:
        if lotes == max_lotes:
            break
        productos[producto] += lote
        lotes += 1
    return lotes

# Pruebas y ejemplos
print("stock_total tornillos (repetido):", stock_total(almacen, "tornillos"))
print("stock_total taladros (inexistente):", stock_total(almacen, "taladros"))

print("críticos (minimo=20):", productos_criticos(almacen))
print("críticos (minimo=50):", productos_criticos(almacen, minimo=50))

# Existe en el pasillo
print("\nreponer clavos en pasillo1 (15 -> mínimo 40):")
n = reponer(almacen, "pasillo1", "clavos", 40)
print("  lotes añadidos:", n, "| nuevo stock en pasillo1:", almacen["pasillo1"]["clavos"])

# No existe en el pasillo (parte de 0)
print("reponer cable en pasillo1 (no está, mínimo 30):")
n = reponer(almacen, "pasillo1", "cable", 30)
print("  lotes añadidos:", n, "| nuevo stock en pasillo1:", almacen["pasillo1"]["cable"])

# Corte por max_lotes
print("reponer martillos en pasillo4 (9 -> mínimo 500, tope 5 lotes):")
n = reponer(almacen, "pasillo4", "martillos", 500)
print("  lotes añadidos:", n, "| nuevo stock en pasillo4:", almacen["pasillo4"]["martillos"])
