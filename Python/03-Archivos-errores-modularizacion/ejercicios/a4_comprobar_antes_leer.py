"""
Actividad 4 — Comprobar antes de leer
Escribe un programa que, usando os.path.exists(), 
compruebe si existe un archivo notas.txt. Si existe, muéstralo; si no,
muestra un mensaje explicando que aún no se ha creado, sin usar try/except. 
"""
# Importamos os para trabajar con ficheros
import os
# Ruta del fichero notas.txt
path_notas = "../output/notas.txt"

if os.path.exists(path_notas):
    with open (path_notas, "r", encoding="utf-8") as fichero:
        print(fichero.read())
# Si no encuentra el fichero, mostramos el "error"
else:
    print("El fichero no se ha creado todavia, crealo primero")