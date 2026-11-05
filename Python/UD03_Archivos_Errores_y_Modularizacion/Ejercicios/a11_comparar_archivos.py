"""
Actividad 11 — Comparar dos archivos
Escribe un programa que lea dos archivos de texto línea a 
línea y compare su contenido: si son idénticos, debe
indicarlo; si difieren, debe mostrar el número de la primera línea en la que no coinciden
"""
# Importamos os para trabajar con ficheros
import os
path_fichero1 = "../output/test.txt"
path_fichero2_igual = "../output/test2.txt"
path_fichero3_diferentes = "../output/test3.txt"

# Funcion para comparar 2 ficheros
def comparar_dos_ficheros(fichero1, fichero2):
    with open(fichero1, "r", encoding="utf-8") as fich1:
        with open(fichero2, "r", encoding="utf-8") as fich2:

            linea = 1

            while True:
                # Leemos iterativamente las lineas de los dos ficheros y las comparamos
                linea1 = fich1.readline()
                linea2 = fich2.readline()

                if linea1 != linea2:
                    if linea1 == "" and linea2 == "":
                        print("Los archivos son idénticos")
                    else:
                        print(f"Diferencia en la línea {linea}")
                    break

                if linea1 == "":
                    print("Los archivos son idénticos")
                    break

                linea += 1

print("Prueba 1:")
comparar_dos_ficheros(path_fichero1, path_fichero2_igual)
print("Prueba 2:")
comparar_dos_ficheros(path_fichero1, path_fichero3_diferentes)