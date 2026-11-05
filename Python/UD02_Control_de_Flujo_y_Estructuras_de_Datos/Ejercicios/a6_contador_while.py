"""
Actividad 6. Contador con while
Escribe un programa que pida números al usuario, uno tras otro, hasta que introduzca un
0. Al terminar, muestra cuántos números se han introducido (sin contar el 0) y su suma
total.
"""
# Inicializamos num a 1 (un valor distinto de 0) para que el while entre al menos
# una vez. Si lo pusiéramos a 0 el bucle no se ejecutaria nunca
num = 1
contador = 0  # cuenta los numeros introducidos

while num != 0:
    num = int(input("Introduce un numero: "))

    # El if de dentro hace que el 0 que cierra el bucle no cuente como numero
    # introducido: sin el, el contador sumaria uno de mas
    if num != 0:
        contador += 1

# Cuando el usuario mete el 0 el while deja de cumplirse y execution sale aqui
print(f"Cantidad de numeros introducidos: {contador}")