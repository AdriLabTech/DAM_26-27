"""
Actividad 14 — Historial de notas.
Escribe un programa que pida una nota al usuario y 
la añada (modo "a") a un archivo historial.txt, junto con un número de intento.
Cada vez que se ejecute el programa, debe añadirse una nueva línea sin borrar las
anteriores
"""
import os

path_fichero = "../output/historial.txt"

# El siguiente intento es el numero de lineas que ya hay + 1
def contar_intentos(fichero):
    if not os.path.exists(fichero):
        return 0
    with open(fichero, "r", encoding="utf-8") as f:
        return len(f.readlines())

def agregar_registro(nota, fichero):
    numero_intento = contar_intentos(fichero) + 1
    with open(fichero, "a", encoding="utf-8") as f:
        f.write(f"Intento {numero_intento}: {nota}\n")

try:
    agregar_registro(float(input("Introduce una nota: ")), path_fichero)
except ValueError:
    print("[ERROR]: la nota tiene que ser un numero")

if os.path.exists(path_fichero):
    with open(path_fichero, "r", encoding="utf-8") as f:
        print(f.read())
