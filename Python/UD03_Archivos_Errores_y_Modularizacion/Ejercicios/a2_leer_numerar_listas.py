"""
Actividad 2 — Leer y numerar líneas
Crea manualmente un archivo poema.txt con al menos 5 líneas de texto. 
Escribe un programa que lo lea y muestre cada línea precedida de su número: 
1. ..., 2. ..., etc
"""
import os

path_fichero = "../output/poema.txt"

if os.path.exists(path_fichero):
    with open(path_fichero, "r", encoding="utf-8") as archivo:
        # enumerate lleva la cuenta por nosotros; start=1 para que empiece en 1
        for numero, linea in enumerate(archivo, start=1):
            # La linea ya trae su salto de linea, por eso el end=""
            print(f"{numero}. {linea}", end="")
    print()
else:
    print("El fichero poema.txt no existe")
