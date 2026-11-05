"""
Actividad 9 — Buscador de texto en un archivo.
Escribe un programa que pida al usuario una palabra y 
muestre solo las líneas de un archivo de texto
que contienen esa palabra, leyendo el archivo línea a línea
"""
# Importamos os para trabajar con ficheros
import os
path_fichero = "../output/test.txt"

def buscar_palabra_texto(palabra):
    if os.path.exists(path_fichero):
        with open(path_fichero, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.__contains__(palabra):
                    print(linea)

buscar_palabra_texto("ejercicios")