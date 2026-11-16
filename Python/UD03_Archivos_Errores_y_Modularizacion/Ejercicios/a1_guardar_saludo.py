"""
Actividad 1 - Guardar un saludo
Escribe un programa que pida el nombre
del usuario por teclado y guarde en un archivo saludo.txt el texto "Hola, <nombre>,
bienvenido/a al curso". Usa with open(...). 
"""
path_fichero = "../output/a1_guardar_saludo.txt"

nombre = input("Introduce tu nombre: ")

# El modo "w" crea el fichero si no existe y lo sobrescribe si ya estaba,
# asi que no hace falta comprobar nada antes
with open(path_fichero, "w", encoding="utf-8") as archivo:
    archivo.write(f"Hola, {nombre}, bienvenido/a al curso")

# Lo volvemos a leer para ver que se ha guardado bien
with open(path_fichero, "r", encoding="utf-8") as archivo:
    print(archivo.read())
