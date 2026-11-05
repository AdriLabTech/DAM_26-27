"""
Actividad 7 — Contar palabras de un archivo
Escribe un programa que abra un archivo de texto y cuente 
cuántas palabras contiene en total, leyendo línea a línea y
usando split() en cada una para contar los elementos
"""
# Importamos os para trabajar con archivos
import os
path_fichero = "../output/poema.txt"

def contar_palabras(fichero):
    contador = 0
    if os.path.exists(fichero):
        with open (fichero, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                contador += len(linea.split())
    return contador

contador = contar_palabras(path_fichero)
print(contador)