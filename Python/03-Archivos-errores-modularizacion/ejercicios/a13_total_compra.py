"""
Actividad 13 — Total de la compra.
Crea un archivo compra.txt donde cada línea tenga el 
formato producto,precio (por ejemplo pan,1.20). Escribe un programa que
lea el archivo y calcule el importe total de la compra
"""
# Importamos os para trabajar con ficheros
import os
path_fichero_compra = "../output/compra.txt"

def calcular_importe_linea(linea):
    # Separamos la linea en lo que hay antes y despues de la coma
    # pan,1.20 -> ["pan", "1.20"]
    partes_cadena = linea.split(",")
    try:
        precio = float(partes_cadena[-1]) # Obtenemos la ultima parte (la parte del precio)
    except ValueError:
        print("El precio no es numerico")
        return 0.0 # Asi evitamos None

    return precio

def calcular_importe_fichero(fichero):
    precio_total = 0.0
    if os.path.exists(fichero):
        with open (fichero, "r", encoding="utf-8") as f:
            for linea in f:
                precio_total += calcular_importe_linea(linea)

    return precio_total

precio_final = calcular_importe_fichero(path_fichero_compra)

print(f"El precio total de la compra es: {precio_final}")