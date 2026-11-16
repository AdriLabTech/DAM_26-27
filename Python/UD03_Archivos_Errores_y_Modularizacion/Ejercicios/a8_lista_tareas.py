"""
Actividad 8 — Lista de tareas
Escribe un programa que vaya pidiendo tareas al usuario y las guarde, 
una por línea, en un archivo tareas.txt, hasta que el usuario escriba
"fin"
"""
path_fichero = "../output/tareas.txt"

# Primero juntamos las tareas en una lista y al final las guardamos de golpe
lista_tareas = []
while True:
    entrada_usuario = input("Ingrese el nombre de la tarea: ")
    if entrada_usuario == "fin":
        break
    lista_tareas.append(entrada_usuario)

with open(path_fichero, "w", encoding="utf-8") as archivo:
    for tarea in lista_tareas:
        archivo.write(tarea + "\n")

with open(path_fichero, "r", encoding="utf-8") as archivo:
    print(archivo.read())
