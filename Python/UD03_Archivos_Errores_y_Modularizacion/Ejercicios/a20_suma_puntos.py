"""
Actividad 20 — Suma de puntos de un juego.
Crea un archivo resultados.txt con una puntuación por línea, 
incluyendo alguna línea corrupta. Escribe un programa que
sume todas las puntuaciones válidas, usando try/except para saltarse las líneas corruptas
sin detener el programa
"""
import os

fichero = "../output/a20_resultados.txt"

def suma_puntuaciones(fichero):
    suma = 0
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as f:
            for linea in f:
                try:
                    suma += float(linea)
                except ValueError:
                    print(f"Linea corrupta saltada: {linea.strip()!r}")
    else:
        print("El fichero no existe")
    return suma

print(f"La suma de las puntuaciones es: {suma_puntuaciones(fichero)}")
