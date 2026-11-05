"""
Actividad 8 — Lista de tareas
Escribe un programa que vaya pidiendo tareas al usuario y las guarde, 
una por línea, en un archivo tareas.txt, hasta que el usuario escriba
"fin"
"""
# Importamos os para trabajar con archivos
import os
path_fichero = "../output/tareas.txt"

def leer_fichero(fichero):
    if os.path.exists(fichero):
        with open (fichero, "r", encoding="utf-8") as fichero:
            print(fichero.read())

def guardar_tarea(lista_tareas):
    if os.path.exists(path_fichero):
        with open(path_fichero, "w", encoding="utf-8") as archivo:
            for tarea in lista_tareas:
                archivo.write(tarea + "\n")
    else:
    # Creamos el archivo
        with open (path_fichero, "w", encoding="utf-8"):
            guardar_tarea(lista_tareas)

entrada_usuario = "test"
lista_tareas = []
while entrada_usuario != "fin":
    entrada_usuario = input("Ingrese el nombre de la tarea: ")
    if entrada_usuario != "fin":
        lista_tareas.append(entrada_usuario)

guardar_tarea(lista_tareas)
leer_fichero(path_fichero)