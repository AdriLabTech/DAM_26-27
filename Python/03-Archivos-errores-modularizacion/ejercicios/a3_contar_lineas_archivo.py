"""
Actividad 3 — Contar líneas de un archivo. (Obligatoria) Escribe un programa que abra un
archivo de texto (el que quieras) y muestre cuántas líneas contiene en total
"""
# Importamos os para trabajar con ficheros
import os

# Ruta por defecto del fichero de lectura
default_path_file = "../output/a3_fichero_default.txt"

def contar_lineas_fichero(path_fichero = default_path_file):
    if os.path.exists(path_fichero):
        with open(path_fichero, "r", encoding="utf-8") as fichero:
            contador_lineas = 0
            for linea in fichero:
                contador_lineas += 1
    # Devolvemos el numero de lineas
    return contador_lineas

lineas_fichero_default = contar_lineas_fichero()
lienas_fichero_poema = contar_lineas_fichero("../output/poema.txt")

print(f"Numero de lineas del fichero por defecto: {lineas_fichero_default}")
print(f"Numero de lineas del poema: {lienas_fichero_poema}")