"""
Actividad 12 — Copiar un archivo en mayúsculas
Escribe un programa que lea un archivo de texto y 
guarde una copia de su contenido, convertido a
mayúsculas con upper(), en un archivo nuevo con distinto nombre.
"""
# Importamos os para comprobar si los ficheros existen
import os
path_fichero_entrada = "../output/test.txt"
path_fichero_salida = "../output/a12_output.txt"

def copiar_texto_mayusculas(fichero_entrada, fichero_salida):
    if os.path.exists(fichero_entrada):
        # Leemos del original y escribimos la copia ya en mayusculas
        # (el modo "w" crea el fichero nuevo si no existe)
        with open(fichero_entrada, "r", encoding="utf-8") as entrada:
            with open(fichero_salida, "w", encoding="utf-8") as fichero:
                fichero.write(entrada.read().upper())
    else:
        print("[ERROR]: El fichero de entrada no existe")

def leer_fichero(fichero):
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("[ERROR]: El fichero no existe, crealo primero...")

copiar_texto_mayusculas(path_fichero_entrada, path_fichero_salida)
leer_fichero(path_fichero_salida)
