"""
Actividad 11. Tabla de multiplicar invertida
Pide un número y muestra su tabla de multiplicar del 10 al 1, en orden descendente, usando
range() con paso negativo
"""
# Capturamos la entrada del usuario casteandola a entero
num_tabla = int(input("Introduce el numero para calcular su tabla de multiplicar: "))

for i in range(10, 0, -1):
    print(f"{i} x {num_tabla} = {num_tabla * i}")