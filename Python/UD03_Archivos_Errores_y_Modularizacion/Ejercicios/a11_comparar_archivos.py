"""
Actividad 11 — Comparar dos archivos
Escribe un programa que lea dos archivos de texto línea a 
línea y compare su contenido: si son idénticos, debe
indicarlo; si difieren, debe mostrar el número de la primera línea en la que no coinciden
"""
path_fichero1 = "../output/test.txt"
path_fichero2_igual = "../output/test2.txt"
path_fichero3_diferentes = "../output/test3.txt"

def comparar_dos_ficheros(fichero1, fichero2):
    with open(fichero1, "r", encoding="utf-8") as fich1, \
         open(fichero2, "r", encoding="utf-8") as fich2:
        numero_linea = 1
        while True:
            # readline() devuelve "" cuando ya no quedan lineas
            linea1 = fich1.readline()
            linea2 = fich2.readline()

            if linea1 != linea2:
                print(f"Diferencia en la línea {numero_linea}")
                return
            # Si son iguales y vacias, hemos llegado al final de los dos
            if linea1 == "":
                print("Los archivos son idénticos")
                return
            numero_linea += 1

print("Prueba 1:")
comparar_dos_ficheros(path_fichero1, path_fichero2_igual)
print("Prueba 2:")
comparar_dos_ficheros(path_fichero1, path_fichero3_diferentes)
