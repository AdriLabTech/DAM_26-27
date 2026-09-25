"""
Actividad 10. Suma de números pares
Pide un número N y, con un bucle for y range() con paso 2, calcula la suma de los primeros
N números pares.
"""
# Capturamos la entrada del usuario casteandolo a entero
n = int(input("Introduzca el numero limite para calcular sus pares: "))
suma = 0

for i in range(0,n + 1,2):
    suma += i

print(f"La suma de toso los numeros pares es: {suma}")