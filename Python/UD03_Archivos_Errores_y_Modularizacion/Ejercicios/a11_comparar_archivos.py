"""
Actividad 11 — Comparar dos archivos
Escribe un programa que lea dos archivos de texto línea a 
línea y compare su contenido: si son idénticos, debe
indicarlo; si difieren, debe mostrar el número de la primera línea en la que no coinciden
"""
path_fichero1 = "../output/test.txt"
path_fichero2_igual = "../output/test2.txt"
path_fichero3_diferentes = "../output/test3.txt"

# Funcion para comparar 2 ficheros
def comparar_dos_ficheros(fichero1, fichero2):
    # Abrimos los dos ficheros a la vez
    with open(fichero1, "r", encoding="utf-8") as fich1:
        with open(fichero2, "r", encoding="utf-8") as fich2:
            linea = 1
            while True:
                # Leemos una linea de cada fichero y las comparamos
                # (readline() devuelve "" cuando ya no quedan lineas)
                linea1 = fich1.readline()
                linea2 = fich2.readline()

                # Si son distintas, esta es la primera linea que no coincide
                if linea1 != linea2:
                    print(f"Diferencia en la línea {linea}")
                    break

                # Si las dos estan vacias, llegamos al final sin diferencias
                if linea1 == "":
                    print("Los archivos son idénticos")
                    break

                linea += 1

print("Prueba 1:")
comparar_dos_ficheros(path_fichero1, path_fichero2_igual)
print("Prueba 2:")
comparar_dos_ficheros(path_fichero1, path_fichero3_diferentes)
