"""
Actividad 6 — Copiar un archivo
Crea un archivo origen.txt con algunas líneas de texto. 
Escribe un programa que copie todo su contenido a un archivo destino.txt,
usando with open(...) tanto para leer como para escribir.
"""
import os

path_fichero_origen = "../output/origen.txt"
path_fichero_destino = "../output/destino.txt"

def copiar_texto(path_entrada, path_salida):
    # Sin el origen no hay nada que copiar
    if not os.path.exists(path_entrada):
        print("Se necesita el archivo a clonar para poder clonar")
        return
    # Abrimos los dos a la vez: el origen para leer y el destino para escribir
    with open(path_entrada, "r", encoding="utf-8") as origen, \
         open(path_salida, "w", encoding="utf-8") as destino:
        for linea in origen:
            destino.write(linea)

copiar_texto(path_fichero_origen, path_fichero_destino)

if os.path.exists(path_fichero_destino):
    print("Contenido: ")
    with open(path_fichero_destino, "r", encoding="utf-8") as fichero:
        print(fichero.read())
