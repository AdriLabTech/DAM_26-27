"""
Actividad 4. Tabla de multiplicar
Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10, usando un bucle for
y range()
"""
# Capturamos la entrada del usuario y la casteamos a entero
num_tabla = int(input("Introduce un numero parar mostrar su tabla de multiplicar: "))
for i in range (1,11): # Agregamos uno mas porque en las tuplas se empieza por el cero
    print(f"{num_tabla} x {i}: {num_tabla * i}")
