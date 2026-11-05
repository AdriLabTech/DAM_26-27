"""
# --------------------------------
# Actividad 7. Calculadora basica
# --------------------------------

Capturamos la entrada del usuario y casteamos los valores a enteros
"""
numero_usuario_1 = int(input("Introduce el primer numero: "))
numero_usuario_2 = int(input("Introduce el segundo numero: "))

# Realizamos las operaciones
suma = numero_usuario_1 + numero_usuario_2
resta = numero_usuario_1 - numero_usuario_2
multiplicacion = numero_usuario_1 * numero_usuario_2
division = numero_usuario_1 / numero_usuario_2
division_entera = numero_usuario_1 // numero_usuario_2
modulo = numero_usuario_1 % numero_usuario_2
potencia = numero_usuario_1 ** numero_usuario_2

# Mostramos los resultados por pantalla
print(f"Suma: {suma} ")
print(f"Resta: {resta} ")
print(f"Multiplicacion: {multiplicacion} ")
print(f"Division: {division} ")
print(f"Division entera: {division_entera} ")
print(f"Modulo: {modulo} ")
print(f"Potencia: {potencia}")

