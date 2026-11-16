"""
Actividad 7 — Contar palabras de un archivo
Escribe un programa que abra un archivo de texto y cuente 
cuántas palabras contiene en total, leyendo línea a línea y
usando split() en cada una para contar los elementos
"""
import os

path_fichero = "../output/poema.txt"

def contar_palabras(fichero):
    contador = 0
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # split() separa la linea en palabras y len() las cuenta
                contador += len(linea.split())
    return contador

print(f"El fichero tiene {contar_palabras(path_fichero)} palabras")
