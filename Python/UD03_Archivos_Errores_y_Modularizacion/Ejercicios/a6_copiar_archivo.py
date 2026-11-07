"""
Actividad 6 — Copiar un archivo
Crea un archivo origen.txt con algunas líneas de texto. 
Escribe un programa que copie todo su contenido a un archivo destino.txt,
usando with open(...) tanto para leer como para escribir.
"""
# Importamos os para comprobar si los ficheros existen
import os
path_fichero_origen = "../output/origen.txt"
path_fichero_destino = "../output/destino.txt"

# Funcion para saber si existe un fichero o no
def existe_fichero(path_fichero):
    return os.path.exists(path_fichero)

# Funcion para leer y mostrar un fichero
def leer_fichero(path_fichero):
    if existe_fichero(path_fichero):
        print("Contenido: ")
        with open(path_fichero, "r", encoding="utf-8") as fichero:
            print(fichero.read())

# Funcion para copiar el texto de un fichero a otro
def copiar_texto(path_entrada, path_salida):
    # Sin el origen no hay nada que copiar
    if not existe_fichero(path_entrada):
        print("Se necesita el archivo a clonar para poder clonar")
        return
    # Abrimos los dos ficheros a la vez: uno para leer y otro para escribir.
    # Modo "w": si el destino no existe se crea, y si existe se sustituye su contenido
    with open(path_entrada, "r", encoding="utf-8") as origen:
        with open(path_salida, "w", encoding="utf-8") as destino:
            for linea in origen:
                destino.write(linea)

copiar_texto(path_fichero_origen, path_fichero_destino)
leer_fichero(path_fichero_destino)
