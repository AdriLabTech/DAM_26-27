"""
Actividad 27 - Contar ocurrencias sin count()
Escribe una función contar_ocurrencias(lista, valor) que cuente cuántas veces aparece
valor en lista, sin usar el método count() de las listas
"""


# Reimplementamos a mano lo que hace lista.count(valor)
def contar_ocurrencias(lista, valor):
    ocurrencias = 0

    for elemento in lista:
        # == compara el valor, asi que solo suma cuando coinciden exactamente
        if elemento == valor:
            ocurrencias += 1

    return ocurrencias


lista_numeros = [1, 2, 3, 1, 1, 6, 9, 10, 11, 3]
print(f"Lista de numeros: {lista_numeros}")
print(f"Cantidad de ocurrencias del numero 1: {contar_ocurrencias(lista_numeros, 1)}")