"""
Actividad 9 — Buscador de texto en un archivo.
Escribe un programa que pida al usuario una palabra y 
muestre solo las líneas de un archivo de texto
que contienen esa palabra, leyendo el archivo línea a línea
"""
import os

path_fichero = "../output/test.txt"

def buscar_palabra_texto(palabra):
    if not os.path.exists(path_fichero):
        print("El fichero no existe")
        return
    encontradas = 0
    with open(path_fichero, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if palabra in linea:
                print(linea.strip())
                encontradas += 1
    if encontradas == 0:
        print(f"No hay ninguna linea con '{palabra}'")

buscar_palabra_texto(input("Palabra a buscar: "))
