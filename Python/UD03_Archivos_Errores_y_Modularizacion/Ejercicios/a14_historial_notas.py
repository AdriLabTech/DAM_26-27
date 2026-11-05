"""
Actividad 14 — Historial de notas.
Escribe un programa que pida una nota al usuario y 
la añada (modo "a") a un archivo historial.txt, junto con un número de intento.
Cada vez que se ejecute el programa, debe añadirse una nueva línea sin borrar las
anteriores
"""
# Importamos os para trabajar con ficheros
import os
path_fichero = "../output/historial.txt"

def agregar_registro(nota, fichero):
    if os.path.exists(fichero):
        with open (fichero, "a", encoding="utf-8") as f:
            f.write(str(nota) + "\n") # Agregamos la nota en formato str y con un salto de linea
    else:
        with open(fichero, "w", encoding="utf-8"):
            agregar_registro(nota, fichero)

def leer_fichero(fichero):
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as f:
            print(f.read())

agregar_registro(6.8, path_fichero)
agregar_registro(3.2, path_fichero)
agregar_registro(9.7, path_fichero)

leer_fichero(path_fichero)