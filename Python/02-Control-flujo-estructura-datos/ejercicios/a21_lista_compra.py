"""
Actividad 21 - Lista de la compra
Crea una lista vacía. En un bucle, pide al usuario productos uno a uno (mientras no escriba
"fin") y añádelos con append(). Al terminar, muestra la lista completa numerada (usando
for con enumerate()) y el número total de productos con len()
"""
# La lista empieza vacia, aqui es donde se van guardando los productos
lista_productos = []

# Inicializamos la entrada a "" para que el while entre la primera vez ("" es
# distinto de "fin")
entrada_usuario = ""

while entrada_usuario != "fin":
    entrada_usuario = input("Introduce un nuevo producto: ")
    # append() anade el producto al final de la lista. Ojo: la palabra "fin"
    # tambien se guarda, porque el while para al principio de la vuelta
    # siguiente, despues de haberla anadido ya
    lista_productos.append(entrada_usuario)

# enumerate() devuelve a la vez el indice y el elemento, asi que no hace falta
# ir buscando el valor en la lista. El indice empieza en 0
for idx, i in enumerate(lista_productos):
    print(idx, i)

# len() devuelve cuantas elementos tiene la lista ahora mismo
print(f"Cantidad de productos: {len(lista_productos)}")