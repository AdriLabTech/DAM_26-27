"""
Actividad 1 - Guardar un saludo
Escribe un programa que pida el nombre
del usuario por teclado y guarde en un archivo saludo.txt el texto "Hola, <nombre>,
bienvenido/a al curso". Usa with open(...). 
"""
# Importamos os para trabajar con ficheros
import os
# guardamos la ruta del fichero para usarla en todo el programa
path_fichero = "../output/a1_guardar_saludo.txt"

# Funcion para leer el contenido del fichero
def leer_contenido_fichero():
    if os.path.exists(path_fichero):
        with open(path_fichero, "r", encoding="utf-8") as archivo_lectura:
            print(archivo_lectura.read())
            
# Funcion para guardar el saludo dentro del fichero
def guardar_nombre(nombre_a_guardar):
    if os.path.exists(path_fichero):
        with open (path_fichero, "w", encoding="utf-8") as archivo:
            archivo.write(f"Hola, {nombre_a_guardar}, bienvenido/a al curso")
# Guardamos el nombre que introduzca el usuario
nombre = input("Introduce tu nombre: ")

# Si existe el fichero, guardamos el nombre, si no, creamos el fichero y lo guardamos
if os.path.exists(path_fichero):
    guardar_nombre(nombre)
else:
    print("No existe el fichero, se esta creando...")
    with open(path_fichero, "w", encoding="utf-8"):
        guardar_nombre(nombre)
        
# Leemos el contenido final del fichero
leer_contenido_fichero()