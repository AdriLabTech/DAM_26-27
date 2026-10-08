"""
Actividad 14. Máximo de una lista a mano
Dada una lista de números ya escrita en el código, recorre la lista con un bucle for y
determina cuál es el valor máximo, sin usar la función max() de Python
"""
# Definimos la lista de numeros
lista_numeros = [1, 2, 3, 4, 2, 7, 5, 9, 0, 10, 17, 2, 14, 3, 19, 0, 2, 4, 5, 7]

# El algoritmo necesita un punto de partida, y ese punto es el primer elemento
# de la lista. Si lo inicializaramos a 0 el resultado seria incorrecto en
# listas donde todos los numeros son negativos
numero_maximo = lista_numeros[0]

for i in lista_numeros:
    # Cada vez que encontramos un valor mayor que el que teniamos, ese valor
    # pasa a ser el nuevo maximo y nos quedamos con el
    if i > numero_maximo:
        numero_maximo = i

print(f"El numero mas grande de toda la lista es: {numero_maximo}")