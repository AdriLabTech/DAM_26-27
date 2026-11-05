"""
Actividad 30 - Eliminar duplicados sin set
Dada una lista con elementos repetidos, recórrela con un bucle for y construye una nueva
lista que contenga cada valor una sola vez, sin usar set()
"""


def eliminar_repetidos(lista):
    lista_sin_repetir = []

    for elemento in lista:
        # El operador not in devuelve True cuando el elemento NO esta todavia
        # en la lista. Es la forma de comprobarlo sin usar set(): si aun no
        # existe, lo anadimos; si ya estaba, lo saltamos y no se duplica
        if elemento not in lista_sin_repetir:
            lista_sin_repetir.append(elemento)

    return lista_sin_repetir


lista_con_repetidos = [1, 2, 3, 1, 3, 5, 7, 1, 10, 9, 1]
print(f"Lista sin repetidos: {eliminar_repetidos(lista_con_repetidos)}")