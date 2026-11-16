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
    campos = [c.strip() for c in linea.split(",")]
    if len(campos) != 3:
        raise ValueError(f"Cantidad de elementos no valido: {campos}")

    # Si cantidad o precio no son numeros, float() ya lanza ValueError
    cantidad = float(campos[1])
    precio = float(campos[2])
    return cantidad * precio

factura_total = 0

if os.path.exists(fichero):
    with open(fichero, "r", encoding="utf-8") as f:
        for linea in f:
            try:
                factura_total += calcular_factura_producto(linea)
            except ValueError as e:
                print(f"[DESCARTADA]: {e}")

    print(f"Factura total: {factura_total:.2f}")
else:
    print("El fichero ventas.txt no existe")
