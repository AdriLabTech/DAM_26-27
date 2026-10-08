"""
Actividad 4. Tabla de multiplicar
Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10, usando un bucle for
y range()
"""
# Capturamos la entrada del usuario y la convertimos a entero
num_tabla = int(input("Introduce un numero parar mostrar su tabla de multiplicar: "))

# range(1, 11) recorre del 1 al 10 porque range() nunca llega al ultimo valor:
# hay que poner un numero mas del que queremos ver. Asi el bucle da exactamente
# las 10 multiplicaciones que pide el enunciado
for i in range(1, 11):
    # La f-string permite meter dentro de las llaves directamente la operacion
    print(f"{num_tabla} x {i}: {num_tabla * i}")