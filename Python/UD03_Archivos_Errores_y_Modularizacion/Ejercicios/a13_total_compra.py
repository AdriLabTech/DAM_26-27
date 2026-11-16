"""
Actividad 13 — Total de la compra.
Crea un archivo compra.txt donde cada línea tenga el 
formato producto,precio (por ejemplo pan,1.20). Escribe un programa que
lea el archivo y calcule el importe total de la compra
"""
import os

path_fichero_compra = "../output/compra.txt"

def calcular_importe_fichero(fichero):
    precio_total = 0.0
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as f:
            for linea in f:
                # "pan,1.20" -> ["pan", "1.20"]; el precio es la ultima parte
                try:
                    precio_total += float(linea.split(",")[-1])
                except ValueError:
                    print(f"El precio no es numerico: {linea.strip()!r}")
    return precio_total

print(f"El precio total de la compra es: {calcular_importe_fichero(path_fichero_compra):.2f}")
