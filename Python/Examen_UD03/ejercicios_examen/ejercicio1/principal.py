# Adrian - x=8 y=3
"""
Opción 1 — Sumar las ventas de un fichero (3 puntos)

Qué hace el programa. Lee el fichero ventas.txt, que tiene un número en cada línea, y suma los números. Una de las líneas está mal escrita a propósito. El fichero contiene:

12[X] -> x = 8 -> 128
80
abc
4[Y] -> y = 3 -> 43
30

Archivos. Crea dos: ventas.py y principal.py.
2. En principal.py:

    a) Importa la función: from ventas import sumar.
    b) Pega los datos de la opción 1. Son las líneas que crean ventas.txt.
    c) Llama a sumar("ventas.txt") y muestra el total y el número de errores.
    d) Llama también a sumar("no_existe.txt") dentro de un try. Ese fichero no existe y Python lanza FileNotFoundError. Captúralo y muestra el mensaje de la salida.

Salida esperada con [X] = 7 e [Y] = 3 (con tus dígitos solo cambia el total):

Total: 280
Líneas con error: 1
No existe el fichero no_existe.txt
"""

# Importo la libreria os para trabajar con ficheros y directorios del sistema
import os

# Importo el metodo sumar del fichero ventas (no importo todas las funciones)
from ventas import sumar

# Ruta del fichero de ventas
fichero_ventas = "ficheros/ventas.txt"

# Intento sumar todos los valores del fichero, preparando una excepcion por si el archivo no existe
# Tambien nos preparamos por si el fichero contiene lineas no casteables a entero
try:
    total, errores = sumar(fichero_ventas)

    print(f"Total: {total}")
    print(f"Líneas con error: {errores}")

    total2, errores2 = sumar("no_existe.txt")

    # En caso de error, imprimo el mensaje apropiado
except ValueError as error:
    print(f"[ERROR]: {error}")
except FileNotFoundError as error:
    print(f"[ERROR]: {error}")
