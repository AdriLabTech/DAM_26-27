"""
Actividad 27 — Registro de errores en archivo. (Obligatoria) Escribe un programa que
pida al usuario varios números y calcule 100 dividido entre cada uno. Cada vez que se
produzca un error (división entre 0, o texto no numérico), en lugar de solo mostrarlo por
pantalla, debe escribirse una línea describiéndolo en un archivo errores.log (modo “a”), de
forma que al final del programa el archivo contenga un histórico de todos los errores
ocurridos durante la ejecución
"""
import os

fichero = "../output/errores.log"

lista_numeros = []

def añadir_informe(error):
    if os.path.exists(fichero):
        with open(fichero, "a", encoding="utf-8") as f:
            f.write(error)
            print("Error guardado en errores.log")
    else:
        with open(fichero, "w", encoding="utf-8"):
            añadir_informe(error)

while True:
    entrada_usuario = input("Introduce un numero (o sal con 'fin'): ")
    if entrada_usuario == "fin":
        break
    lista_numeros.append(entrada_usuario)

nueva_lista_operada = []

for n in lista_numeros:
    try:
        n = int(n)
        division = n / 100
        nueva_lista_operada.append(division)
    except (ValueError, ZeroDivisionError) as e:
        print(f"[ERROR]: {e}")
        añadir_informe(e)
        continue

