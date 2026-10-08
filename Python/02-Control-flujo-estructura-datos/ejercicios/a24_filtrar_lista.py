"""
Actividad 24 - Filtrar una lista
Dada una lista de números ya escrita en el código (por ejemplo, [12, 7, 45, 3, 89, 21,
6]), crea una nueva lista vacía y, con un bucle for y un if, guarda en ella solo los números
mayores que 10. Muestra ambas listas al final
"""
lista_numeros = [12, 7, 45, 3, 89, 21, 6]

# La lista nueva empieza vacia y aqui van a parar solo los numeros que cumplen
# la condicion
lista_numeros_mayores_diez = []

for numero in lista_numeros:
    # El if acts como filtro: si el numero supera el 10 lo guardamos con
    # append(), y si no simplemente se ignora y el bucle sigue
    if numero > 10:
        lista_numeros_mayores_diez.append(numero)

print(f"Los numeros mayores de 10 son: {lista_numeros_mayores_diez}")