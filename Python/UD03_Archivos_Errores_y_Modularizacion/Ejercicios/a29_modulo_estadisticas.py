"""
Actividad 29 — Módulo de estadísticas. (Obligatoria) Crea un módulo estadisticas.py con
las funciones media(lista), mayor(lista) y menor(lista) para listas de números. Desde un
programa main.py, lee un archivo con un número por línea, construye la lista y usa las tres
funciones del módulo para mostrar los resultados.
"""
import os
# Importamos nuestro modulo (carpeta modulos/, fichero estadisticas.py)
from modulos import estadisticas

fichero = "../output/a29_numeros.txt"

# Si el fichero no existe, lo creamos con unos numeros de ejemplo (uno por linea)
if not os.path.exists(fichero):
    with open(fichero, "w", encoding="utf-8") as f:
        f.write("12\n7.5\n20\n3\nhola\n18.5\n")

# Leemos el fichero y vamos construyendo la lista de numeros
numeros = []
with open(fichero, "r", encoding="utf-8") as f:
    for linea in f:
        try:
            numeros.append(float(linea))
        except ValueError:
            # Una linea que no es un numero (por ejemplo "hola") se salta
            print(f"Linea ignorada: {linea.strip()!r}")

# Usamos las tres funciones del modulo
try:
    print(f"Numeros leidos: {numeros}")
    print(f"Media: {estadisticas.media(numeros):.2f}")
    print(f"Mayor: {estadisticas.mayor(numeros)}")
    print(f"Menor: {estadisticas.menor(numeros)}")
except ValueError as e:
    print(f"[ERROR]: {e}")
