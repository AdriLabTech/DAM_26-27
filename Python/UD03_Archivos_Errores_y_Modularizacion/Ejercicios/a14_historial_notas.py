"""
Actividad 14 — Historial de notas.
Escribe un programa que pida una nota al usuario y 
la añada (modo "a") a un archivo historial.txt, junto con un número de intento.
Cada vez que se ejecute el programa, debe añadirse una nueva línea sin borrar las
anteriores
"""
# Importamos os para comprobar si el fichero existe
import os
path_fichero = "../output/historial.txt"

# Cuenta las lineas que ya hay: el siguiente intento es esa cantidad + 1
def contar_intentos(fichero):
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as f:
            return len(f.readlines())
    return 0

def agregar_registro(nota, fichero):
    numero_intento = contar_intentos(fichero) + 1
    # Modo "a": anade al final sin borrar lo anterior (y crea el fichero si no existe)
    with open(fichero, "a", encoding="utf-8") as f:
        f.write(f"Intento {numero_intento}: {nota}\n")

def leer_fichero(fichero):
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as f:
            print(f.read())

# Pedimos la nota al usuario (antes estaban escritas a mano en el codigo)
try:
    nota_usuario = float(input("Introduce una nota: "))
    agregar_registro(nota_usuario, path_fichero)
except ValueError:
    print("[ERROR]: la nota tiene que ser un numero")

leer_fichero(path_fichero)
