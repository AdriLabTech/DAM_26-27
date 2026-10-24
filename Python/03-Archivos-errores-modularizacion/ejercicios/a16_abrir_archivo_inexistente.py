"""
Actividad 16 — Abrir un archivo que podría no existir. (Obligatoria) Escribe un programa
que intente leer un archivo inventario.txt. Si el archivo no existe, debe capturar el error
FileNotFoundError, avisar al usuario y crear el archivo vacío para la próxima vez.
"""

# Importamos os para trabajar con ficheros
import os

path_fichero = "../output/a16_fichero_inexistente.txt"


def leer_fichero(fichero):
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        with open(fichero, "w", encoding="utf-8"):
            raise FileNotFoundError("El fichero no existe. Se ha creado correctamente")


try:
    leer_fichero(path_fichero)
    leer_fichero(path_fichero)
except FileNotFoundError as e:
    print(f"[ERROR]: {e}")
