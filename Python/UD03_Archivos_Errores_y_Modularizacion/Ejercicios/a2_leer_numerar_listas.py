"""
Actividad 2 — Leer y numerar líneas
Crea manualmente un archivo poema.txt con al menos 5 líneas de texto. 
Escribe un programa que lo lea y muestre cada línea precedida de su número: 
1. ..., 2. ..., etc
"""
# Importamos os para comprobar si el fichero existe
import os

# Guardamos la ruta del fichero
path_fichero = "../output/poema.txt"

def leer_por_lineas():
    if os.path.exists(path_fichero):
        with open(path_fichero, "r", encoding="utf-8") as archivo_a_leer:
            contador_linea = 1
            # Recorremos el fichero linea a linea y sumamos 1 al contador en cada vuelta
            for linea in archivo_a_leer:
                # end="" evita que se junten dos saltos de linea (la linea ya trae el suyo)
                print(f"{contador_linea}. {linea}", end="")
                contador_linea += 1
        print()
    else:
        print("El fichero poema.txt no existe")

leer_por_lineas()
