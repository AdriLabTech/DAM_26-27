"""
Actividad 2. Par o impar
Pide un número al usuario y muestra si es par o impar, usando el operador %.
"""
# Capturamos la entrada del usuario y la convertimos a entero para poder
# trabajar con operaciones matematicas
num_usuario = int(input("Introduce un numero: "))

# El resto de dividir entre 2 da 0 si el numero es par y 1 si es impar, asi que
# basta con comprobar si es 0. Lo metemos todo en un solo print() con una
# condicional ternaria, que es un if/else escrito en una sola linea
print("El Numero es PAR" if num_usuario % 2 == 0 else "El numero es IMPAR")