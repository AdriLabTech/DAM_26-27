"""
Actividad 1. Clasificador de edades

Pide al usuario su edad y muestra "Bebé" (0-2), "Niño/a" (3-12), "Adolescente" (13-17),
"Adulto" (18-64) o "Persona mayor" (65 o más), usando una única cadena de if/elif/else.
"""

# Capturamos la edad del usuario y la convertimos a entero con int(), porque
# input() siempre devuelve texto y sin convertirlo no podriamos compararlo
# con numeros
edad = int(input("Introduce tu edad: "))

# La primera condicion es la unica que comprueba los dos limites, porque es la
# que filtra los bebes. A partir de ahi cada elif solo mira el limite superior:
# si la edad ya no es de bebe, basta con saber si es menor que 12, 17 o 64
if edad < 0:
    print("Edad no valida")
elif edad >= 0 and edad <= 2:
    print("Bebé")
elif edad <= 12:
    print("Niño/a")
elif edad <= 17:
    print("Adolecente")
elif edad <= 64:
    print("Adulto")
else:
    # Si no ha entrado en ningun caso anterior, la edad es mayor que 64
    print("Persona Mayor")