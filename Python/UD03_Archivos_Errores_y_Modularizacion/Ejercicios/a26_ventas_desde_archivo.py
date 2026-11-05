"""
Actividad 26 — Ventas desde un archivo con datos “sucios”.
Crea un archivo ventas.txt con líneas producto,cantidad,precio, pero incluye
deliberadamente alguna línea mal formateada (con una coma de menos, o con texto en
vez de número). Escribe un programa que calcule el total facturado (cantidad × precio,
sumado para todas las líneas), capturando con try/except las líneas que no se puedan
procesar y avisando de cuáles se han descartado, sin que el programa se detenga
"""
import os

fichero = "../output/ventas.txt"

def calcular_factura_producto(linea):
    campos = linea.split(",")
    campos = [c.replace('\n','') for c in campos]
    if len(campos) != 3:
        raise ValueError (f"Cantidad de elementos no valido: {campos}")
    
    cantidad = float(campos[1])
    precio = float(campos[2])
    print(f"Producto: {campos}")
    return cantidad * precio

factura_total = 0

if os.path.exists(fichero):
    with open(fichero, "r", encoding="utf-8") as f:
        for linea in f:
            try:
                factura_total += calcular_factura_producto(linea)
            except (ValueError, TypeError) as e:
                print(f"[ERROR]: {e}")
                continue

        print(f"Factura total: {factura_total}")