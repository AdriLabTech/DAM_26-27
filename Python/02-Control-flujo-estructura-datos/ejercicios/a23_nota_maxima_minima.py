"""
Actividad 23 - Nota máxima y mínima
Pide al usuario cinco notas, una a una, y guárdalas en una lista. Sin usar las funciones max()
ni min() de Python, escribe tu propio bucle que recorra la lista y determine cuál es la nota
más alta y cuál la más baja
"""
lista_numeros = []

# Pedimos cinco notas con range(1, 6): el 6 queda fuera porque range() nunca
# llega al ultimo valor, asi que con 1,5,6 se recorre cinco veces
for i in range(1, 6):
    numero = int(input("Introduce un numero: "))
    lista_numeros.append(numero)

# Igual que en el ejercicio 14, los dos valores de partida son el primer
# elemento de la lista
valor_maximo = lista_numeros[0]
valor_minimo = lista_numeros[0]

# Recorremos la lista UNA sola vez buscando los dos extremos. Los dos if son
# independientes (no un if/elif), porque un numero puede ser a la vez el mayor
# y el menor en distintas vueltas
for valor in lista_numeros:
    if valor > valor_maximo:
        valor_maximo = valor
    if valor < valor_minimo:
        valor_minimo = valor

print(f"El numero mas alto es: {valor_maximo} y el numero mas bajo es: {valor_minimo}")