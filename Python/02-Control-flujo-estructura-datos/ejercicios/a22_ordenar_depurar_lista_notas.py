"""
Actividad 22 - Ordenar y depurar una lista de notas.
Dada una lista de notas ya escrita en el código, algunas repetidas (por ejemplo, [5, 8, 8,
3, 9, 5, 7]): ordénala de mayor a menor con sort(reverse=True), inserta con insert()
una nota de recuperación (un 5) en la segunda posición, y elimina con pop() la última nota
de la lista. Muestra la lista después de cada paso
"""
lista_notas = [5, 8, 8, 3, 9, 5, 7]

# Mostramos la lista como esta al principio, antes de tocarla
print(f"Lista SIN ordenar: {lista_notas}")

# sort() ordena la lista en su sitio (no crea una nueva) y reverse=True lo hace
# de mayor a menor en vez de de menor a mayor
lista_notas.sort(reverse=True)
print(f"Lista ordenada: {lista_notas}")

# insert() mete el valor en la posicion que le digamos. El indice 1 es la
# SEGUNDA posicion, porque en una lista la primera es el indice 0. Asi el 5 de
# recuperacion queda justo debajo del 9
lista_notas.insert(1, 5)
print(f"Lista con un elemento en la 2º posicion: {lista_notas}")

# pop() sin argumento quita el ultimo elemento de la lista. Si le pasaras un
# indice quitaria ese elemento en concreto
lista_notas.pop()
print(f"Lista sin el ultimo numero: {lista_notas}")