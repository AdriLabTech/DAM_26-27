"""
Actividad 19 — Media de temperaturas.
Crea un archivo temperaturas.txt con una temperatura por 
línea. Escribe un programa que calcule la media de todas ellas,
usando try/except para descartar (sin detener el programa) las líneas que no contengan
un número válido
"""
import os

fichero = "../output/a19_temperaturas.txt"

def agregar_temperatura(temperatura):
    temperatura = str(temperatura)
    if os.path.exists(fichero):
        with open(fichero, "a", encoding="utf-8") as f:
            f.write(temperatura + "\n")
    else:
        with open(fichero, "w", encoding="utf-8"):
            agregar_temperatura(temperatura)

def calcular_media(fichero):
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as f:
            suma = 0
            lineas = 0
            for linea in f:
                try:
                    temperatura = float(linea)
                    suma += temperatura
                    lineas += 1
                except ValueError:
                    continue

            return suma / lineas if lineas != 0 else 0
try:
    agregar_temperatura(12.8)
    agregar_temperatura(9.4)
    agregar_temperatura(1)
    agregar_temperatura(123.5)
    agregar_temperatura("no valido")

    print(f"La media de las temperaturas es: {calcular_media(fichero)}")
except ValueError as e:
    print(f"[ERROR]: {e}")