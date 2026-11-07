"""
Actividad 9 — Buscador de texto en un archivo.
Escribe un programa que pida al usuario una palabra y 
muestre solo las líneas de un archivo de texto
que contienen esa palabra, leyendo el archivo línea a línea
"""
# Importamos os para comprobar si el fichero existe
import os
path_fichero = "../output/test.txt"

def buscar_palabra_texto(palabra):
    encontradas = 0
    if os.path.exists(path_fichero):
        with open(path_fichero, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # "in" comprueba si la palabra aparece dentro de la linea
                if palabra in linea:
                    # strip() quita el salto de linea para no dejar huecos de mas
                    print(linea.strip())
                    encontradas += 1
    else:
        print("El fichero no existe")
    if encontradas == 0:
        print(f"No hay ninguna linea con '{palabra}'")

# Pedimos la palabra al usuario (antes estaba escrita a mano en el codigo)
palabra_usuario = input("Palabra a buscar: ")
buscar_palabra_texto(palabra_usuario)
