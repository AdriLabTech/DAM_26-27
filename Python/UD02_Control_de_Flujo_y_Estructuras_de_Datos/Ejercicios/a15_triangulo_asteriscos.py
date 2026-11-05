"""
Actividad 15. Triángulo de asteriscos. (Voluntaria — ampliación)
Pide un número de filas N y dibuja, con dos bucles for anidados, un triángulo de asteriscos
de N filas
"""

n = int(input("Introduce el tamaño del triángulo: "))

# El bucle exterior controla las FILAS: va de 1 a n, y como range() no llega al
# final usamos n + 1 para que la fila n tambien se dibuje
for i in range(1, n + 1):
    # En la fila i, los espacios son n - i (van disminuyendo) y los asteriscos
    # son i (van aumentando), de ahi el triangulo centrado
    espacios = n - i
    asteriscos = i

    # Multiplicar un string por un numero lo repite ese numero de veces, asi
    # que aqui juntamos los espacios de delante con los asteriscos de detras
    print(" " * espacios + "* " * asteriscos)