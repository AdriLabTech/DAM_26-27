"""
Actividad 8 — Lista de tareas
Escribe un programa que vaya pidiendo tareas al usuario y las guarde, 
una por línea, en un archivo tareas.txt, hasta que el usuario escriba
"fin"
"""
# Importamos os para comprobar si el fichero existe
import os
path_fichero = "../output/tareas.txt"

# Funcion para mostrar lo que hay en el fichero
def leer_fichero(fichero):
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as archivo:
            print(archivo.read())

# Funcion para guardar todas las tareas, una por linea
def guardar_tarea(lista_tareas):
    # Modo "w": crea el fichero si no existe (y lo vacia si ya existia)
    with open(path_fichero, "w", encoding="utf-8") as archivo:
        for tarea in lista_tareas:
            archivo.write(tarea + "\n")

# Vamos pidiendo tareas y las apuntamos en una lista hasta que escriban "fin"
lista_tareas = []
while True:
    entrada_usuario = input("Ingrese el nombre de la tarea: ")
    if entrada_usuario == "fin":
        break
    lista_tareas.append(entrada_usuario)

guardar_tarea(lista_tareas)
leer_fichero(path_fichero)
