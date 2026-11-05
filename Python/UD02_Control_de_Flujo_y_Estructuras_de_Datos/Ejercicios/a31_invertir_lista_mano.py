"""
Actividad 31 - Invertir una lista a mano
Escribe una función invertir_lista(lista) que devuelva una nueva lista con los elementos
en orden inverso, sin usar reverse() ni el corte [::-1]
"""


def invertir_lista(lista):
    lista_resultante = []

    for elemento in lista:
        # insert(0, elemento) mete el valor en la PRIMERA posicion. Como cada
        # elemento nuevo se coloca delante de los anteriores, al terminar la
        # lista queda del reves, sin usar reverse() ni el corte [::-1]
        lista_resultante.insert(0, elemento)

    return lista_resultante


lista = ["Hola", "Mundo", "Python"]
print(f"Lista invertida: {invertir_lista(lista)}")