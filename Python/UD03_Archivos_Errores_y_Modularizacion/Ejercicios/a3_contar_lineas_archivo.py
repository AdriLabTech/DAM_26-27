"""
Actividad 3 — Contar líneas de un archivo. (Obligatoria) Escribe un programa que abra un
archivo de texto (el que quieras) y muestre cuántas líneas contiene en total
"""
import os

default_path_file = "../output/a3_fichero_default.txt"

def contar_lineas_fichero(path_fichero=default_path_file):
    # El contador va fuera del if para devolver 0 si el fichero no existe
    contador_lineas = 0
    if os.path.exists(path_fichero):
        with open(path_fichero, "r", encoding="utf-8") as fichero:
            for linea in fichero:
                contador_lineas += 1
    return contador_lineas

print(f"Numero de lineas del fichero por defecto: {contar_lineas_fichero()}")
print(f"Numero de lineas del poema: {contar_lineas_fichero('../output/poema.txt')}")
