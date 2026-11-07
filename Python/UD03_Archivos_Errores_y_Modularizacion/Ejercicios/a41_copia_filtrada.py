"""
Actividad 41 — Copia filtrada y limpieza de temporales. (Voluntaria)
Copia solo las lineas utiles de un fichero sucio y borra ficheros temporales
apuntando en un log lo que se borra.
"""
import os

sucio = "../output/apuntes_sucios.txt"
limpio = "../output/apuntes_limpios.txt"
log = "../output/limpieza.log"

# Creamos por codigo el fichero sucio (comentarios, lineas vacias y espacios de mas)
with open(sucio, "w", encoding="utf-8") as f:
    f.write("# Apuntes de la unidad 3\n")
    f.write("   Los ficheros se abren con open   \n")
    f.write("\n")
    f.write("# esto es un comentario\n")
    f.write("with cierra el fichero solo\n")
    f.write("      \n")
    f.write("  try y except controlan los errores  \n")

# Y dos ficheros temporales (tmp3.txt no se crea a proposito)
for nombre in ["tmp1.txt", "tmp2.txt"]:
    with open("../output/" + nombre, "w", encoding="utf-8") as f:
        f.write("temporal\n")

# (1) Un unico "with" con los dos ficheros: el sucio para leer y el limpio para escribir
copiadas = 0
with open(sucio, "r", encoding="utf-8") as entrada, open(limpio, "w", encoding="utf-8") as salida:
    for linea in entrada:
        linea = linea.strip()  # quita espacios y salto de linea de los extremos
        # Una linea es util si no esta vacia y no empieza por #
        if linea != "" and not linea.startswith("#"):
            salida.write(linea + "\n")
            copiadas += 1
print(f"Lineas utiles copiadas: {copiadas}")

# (2) Vaciamos el log: abrir en modo "w" y cerrar lo deja en blanco
open(log, "w", encoding="utf-8").close()

# (3) Borramos cada temporal si existe y lo apuntamos en el log
for nombre in ["tmp1.txt", "tmp2.txt", "tmp3.txt"]:
    ruta = "../output/" + nombre
    with open(log, "a", encoding="utf-8") as f:
        if os.path.exists(ruta):
            os.remove(ruta)
            f.write(f"borrado {nombre}\n")
        else:
            f.write(f"no existía {nombre}\n")

print("Contenido de limpieza.log:")
with open(log, "r", encoding="utf-8") as f:
    print(f.read())
