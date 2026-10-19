"""
Actividad 6 — Copiar un archivo
Crea un archivo origen.txt con algunas líneas de texto. 
Escribe un programa que copie todo su contenido a un archivo destino.txt,
usando with open(...) tanto para leer como para escribir.
"""
# Importamos os para trabajar con ficheros
import os
path_fichero_origen = "../output/origen.txt"
path_fichero_destino = "../output/destino.txt"

# Funcion para saber si existe un fichero o no
def existe_fichero(path_fichero):
    return os.path.exists(path_fichero)

# Funcion para leer un fichero
def leer_fichero(path_fichero):
    if existe_fichero(path_fichero):
        print("Contenido: ")
        with open(path_fichero, "r", encoding="utf-8") as fichero:
            print(fichero.read())

# Funcion para copiar un texto de un fichero a otro
def copiar_texto(path_entrada, path_salida):
    if existe_fichero(path_salida):
    # Si el fichero destino existe, agregamos el contenido
        with open(path_salida, "w", encoding="utf-8") as destino:
            if existe_fichero(path_entrada):
                with open(path_entrada, "r", encoding="utf-8") as origen:
                    for linea in origen:
                        destino.write(linea)
            else:
                print("Se necesita el archivo a clonar para poder clonar")
    else:
        with open(path_fichero_destino, "w", encoding="utf-8"):
            copiar_texto(path_fichero_origen, path_fichero_destino)

copiar_texto(path_fichero_origen, path_fichero_destino)
leer_fichero(path_fichero_destino)