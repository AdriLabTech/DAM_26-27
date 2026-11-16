"""
Actividad 12 — Copiar un archivo en mayúsculas
Escribe un programa que lea un archivo de texto y 
guarde una copia de su contenido, convertido a
mayúsculas con upper(), en un archivo nuevo con distinto nombre.
"""
import os

path_fichero_entrada = "../output/test.txt"
path_fichero_salida = "../output/a12_output.txt"

if os.path.exists(path_fichero_entrada):
    with open(path_fichero_entrada, "r", encoding="utf-8") as entrada, \
         open(path_fichero_salida, "w", encoding="utf-8") as salida:
        salida.write(entrada.read().upper())
    with open(path_fichero_salida, "r", encoding="utf-8") as salida:
        print(salida.read())
else:
    print("[ERROR]: El fichero de entrada no existe")
