"""
Actividad 22 — Lectura manual de ventas.
Crea un archivo ventas.txt con líneas del tipo producto,cantidad,precio. 
Escribe un programa que lea el archivo línea a línea, sin usar el 
módulo csv, compruebe que cada línea tiene exactamente
3 campos y descarte con try/except las que no cumplan el formato
"""
import os

fichero = "../output/ventas.txt"
def lectura_campos(linea):
    campos = linea.split(",")
    campos = [c.replace('\n', '') for c in campos]
    if len(campos) != 3:
        raise ValueError("El numero de campos no coincide")
    else:
        return campos

if os.path.exists(fichero):
    with open(fichero, "r", encoding="utf-8") as f:
        for linea in f:
            try:
                print(lectura_campos(linea))
            except ValueError as e:
                continue
