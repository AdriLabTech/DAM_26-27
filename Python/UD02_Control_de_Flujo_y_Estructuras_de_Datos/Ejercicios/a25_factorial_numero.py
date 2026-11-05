"""
Actividad 25 - Factorial de un numero
Escribe una función factorial(n) que calcule el factorial de un número usando un bucle.
Pruébala con varios valores, incluido el 0 (cuyo factorial es 1)
"""


def factorial(n):
    # El factorial de 0 es 1 por convenio, asi que lo tratamos aparte. Si
    # dejaramos que el bucle se ejecutara, range(1, 1) no daria ninguna vuelta y
    # devolveria el 1 inicial, pero lo escribimos para que quede claro
    if n == 0:
        return 1

    # El acumulador empieza en 1 porque multiplicar por 1 no cambia nada
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado


# Probamos la funcion con distintos valores
print(f"{factorial(5)}")
print(f"{factorial(0)}")
print(f"{factorial(27)}")