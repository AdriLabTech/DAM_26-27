"""
Actividad 2. Par o impar
Pide un número al usuario y muestra si es par o impar, usando el operador %.
"""
# Capturamos la entrada del usuario casteandola a entero para
# poder trabajar con operaciones matematicas
num_usuario = int(input("Introduce un numero: "))
print("El Numero es PAR" if num_usuario % 2 == 0 else "El numero es IMPAR")