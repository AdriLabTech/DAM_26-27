"""
Actividad 10. Suma de números pares
Pide un número N y, con un bucle for y range() con paso 2, calcula la suma de los primeros
N números pares.
"""
# Capturamos el numero limite como entero
n = int(input("Introduzca el numero limite para calcular sus pares: "))

# El acumulador suma empieza en 0, que es lo que suma una lista vacia
suma = 0

# Con paso 2 el bucle solo recorre los numeros pares, y como range() no llega
# al final ponemos n + 1 para que el propio n entre en la cuenta
for i in range(0, n + 1, 2):
    suma += i

print(f"La suma de toso los numeros pares es: {suma}")