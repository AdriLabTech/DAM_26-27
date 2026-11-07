"""
Actividad 1 - Guardar un saludo
Escribe un programa que pida el nombre
del usuario por teclado y guarde en un archivo saludo.txt el texto "Hola, <nombre>,
bienvenido/a al curso". Usa with open(...). 
"""
# Importamos os para poder preguntar si un fichero existe
import os
# Guardamos la ruta del fichero para usarla en todo el programa
path_fichero = "../output/a1_guardar_saludo.txt"

# Funcion para leer y mostrar lo que hay dentro del fichero
def leer_contenido_fichero():
    if os.path.exists(path_fichero):
        # "with" cierra el fichero solo cuando terminamos de usarlo
        with open(path_fichero, "r", encoding="utf-8") as archivo_lectura:
            print(archivo_lectura.read())

# Funcion para guardar el saludo dentro del fichero
def guardar_nombre(nombre_a_guardar):
    if os.path.exists(path_fichero):
        # Modo "w": borra lo que hubiera y escribe el saludo nuevo
        with open(path_fichero, "w", encoding="utf-8") as archivo:
            archivo.write(f"Hola, {nombre_a_guardar}, bienvenido/a al curso")

# Pedimos el nombre al usuario
nombre = input("Introduce tu nombre: ")

# Si el fichero existe, guardamos el nombre; si no, lo creamos primero y luego lo guardamos
if os.path.exists(path_fichero):
    guardar_nombre(nombre)
else:
    print("No existe el fichero, se esta creando...")
    with open(path_fichero, "w", encoding="utf-8"):
        pass  # Solo queremos que se cree el fichero vacio
    guardar_nombre(nombre)

# Mostramos el resultado final
leer_contenido_fichero()
