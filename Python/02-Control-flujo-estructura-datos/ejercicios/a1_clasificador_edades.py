"""
Actividad 1. Clasificador de edades

Pide al usuario su edad y muestra "Bebé" (0-2), "Niño/a" (3-12), "Adolescente" (13-17),
"Adulto" (18-64) o "Persona mayor" (65 o más), usando una única cadena de if/elif/else.
"""

# Primero creamos las variables usando input para capturar la
# entrada del usuario
edad = int(input("Introduce tu edad: "))
if edad >= 0 and edad <= 2:
    print("Bebé")
elif edad <= 12:
    print("Niño/a")
elif edad <= 17:
    print("Adolecente")
elif edad <= 64:
    print("Adulto")
else:
    print("Persona Mayor")