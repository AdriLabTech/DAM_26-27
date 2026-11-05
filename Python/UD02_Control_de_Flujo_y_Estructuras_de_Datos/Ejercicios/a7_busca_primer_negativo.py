"""
Actividad 7. Buscar el primer negativo
Dada una lista de números ya escrita en el código (por ejemplo, [4, 9, 2, -3, 8, -7]),
recorre la lista con un bucle for y usa break para detenerte en cuanto encuentres el primer
número negativo, mostrando su valor y su posición. Si no hay ninguno negativo, muéstralo
también.
"""
lista_numeros = [4, 9, 2, -3, 8, -7]
posicion = 0

# Recorremos con range() usando len() como final, asi el bucle se adapta solo al
# tamaño de la lista. Usamos el indice (n) en vez del valor para poder saber en
# que posicion esta el negativo
for n in range(0, len(lista_numeros)):
    if lista_numeros[n] < 0:
        # Guardamos la posicion y con break salimos del bucle, de modo que ya no
        # se miran los numeros siguientes aunque tambien sean negativos
        posicion = n
        break

print(f"El primer numero negativo es {lista_numeros[posicion]} y se encuentra en la posicion {posicion}")