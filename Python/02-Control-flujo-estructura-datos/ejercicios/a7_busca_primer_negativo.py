"""
Actividad 7. Buscar el primer negativo
Dada una lista de números ya escrita en el código (por ejemplo, [4, 9, 2, -3, 8, -7]),
recorre la lista con un bucle for y usa break para detenerte en cuanto encuentres el primer
número negativo, mostrando su valor y su posición. Si no hay ninguno negativo, muéstralo
también.
"""
lista_numeros = [4, 9, 2, -3, 8, -7]
posicion = 0

for n in range(0,len(lista_numeros)): # el metodo len() devuelve la longitud (en este caso) del array
    if lista_numeros[n] < 0:
        posicion = n
        break
print(f"El primer numero negativo es {lista_numeros[posicion]} y se encuentra en la posicion {posicion}")