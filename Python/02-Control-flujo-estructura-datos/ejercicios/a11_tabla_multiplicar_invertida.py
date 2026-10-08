"""
Actividad 11. Tabla de multiplicar invertida
Pide un número y muestra su tabla de multiplicar del 10 al 1, en orden descendente, usando
range() con paso negativo
"""
# Capturamos la entrada del usuario y la convertimos a entero
num_tabla = int(input("Introduce el numero para calcular su tabla de multiplicar: "))

# El tercer argumento siendo -1 hace que range() retroceda en vez de avanzar, por
# eso el bucle va del 10 al 1. El 0 queda fuera porque range() nunca llega al
# ultimo valor
for i in range(10, 0, -1):
    print(f"{i} x {num_tabla} = {num_tabla * i}")