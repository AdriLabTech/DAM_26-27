"""
Actividad 2 — Leer y numerar líneas
Crea manualmente un archivo poema.txt con al menos 5 líneas de texto. 
Escribe un programa que lo lea y muestre cada línea precedida de su número: 
1. ..., 2. ..., etc
"""
# Importamos os para trabajar con ficheros
import os

# Guardamos la ruta del fichero
path_fichero = "../output/poema.txt"

def leer_por_lineas():
    if os.path.exists(path_fichero):
        with open(path_fichero, "r", encoding="utf-8") as archivo_a_leer:
            contador_linea = 1
            # Recorremos todas las lineas con un foreach y aumentamos el contador
            for linea in archivo_a_leer:
                print(f"{contador_linea}: {linea}")
                contador_linea += 1

leer_por_lineas()