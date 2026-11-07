"""
Actividad 3 — Contar líneas de un archivo. (Obligatoria) Escribe un programa que abra un
archivo de texto (el que quieras) y muestre cuántas líneas contiene en total
"""
# Importamos os para comprobar si el fichero existe
import os

# Ruta por defecto del fichero que se va a leer
default_path_file = "../output/a3_fichero_default.txt"

def contar_lineas_fichero(path_fichero = default_path_file):
    # Empezamos en 0 fuera del "if": asi, si el fichero no existe, devolvemos 0 en vez de fallar
    contador_lineas = 0
    if os.path.exists(path_fichero):
        with open(path_fichero, "r", encoding="utf-8") as fichero:
            # Cada vuelta del bucle es una linea del fichero
            for linea in fichero:
                contador_lineas += 1
    return contador_lineas

lineas_fichero_default = contar_lineas_fichero()
lineas_fichero_poema = contar_lineas_fichero("../output/poema.txt")

print(f"Numero de lineas del fichero por defecto: {lineas_fichero_default}")
print(f"Numero de lineas del poema: {lineas_fichero_poema}")
