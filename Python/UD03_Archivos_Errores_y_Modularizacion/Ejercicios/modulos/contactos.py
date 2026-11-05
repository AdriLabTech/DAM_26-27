"""
Actividad 25 — Módulo de contactos
Crea un módulo contactos.py con tres funciones: 
añadir_contacto(nombre, telefono) (que añade una línea 
nombre,telefono a contactos.txt), listar_contactos() (que muestra  todos 
los contactos guardados) y buscar_contacto(nombre) (que busca y 
muestra el teléfono de un contacto, o un mensaje
si no existe). Desde un programa main.py, importa el módulo y ofrece un pequeño menú
para probar las tres funciones
"""
import os
fichero_contactos = "../output/contactos.txt"
# Modulo de contactos
def añadir_contacto(nombre, telefono):
    if os.path.exists(fichero_contactos):
        with open(fichero_contactos, "a", encoding="utf-8") as f:
            f.write(f"{nombre},{telefono}\n")
            print("Registro guardado")
    else:
        with open(fichero_contactos, "a", encoding="utf-8"):
            añadir_contacto(nombre, telefono)

def listar_contactos():
    if os.path.exists(fichero_contactos):
        with open(fichero_contactos, "r", encoding="utf-8") as f:
            for linea in f:
                print("-----------------------------------")
                print(f"Registro: {linea}")
                print("-----------------------------------")
    else:
        raise FileNotFoundError ("[ERROR]: fichero contactos.txt no existe")

def buscar_contacto(nombre):
    if os.path.exists(fichero_contactos):
        with open(fichero_contactos, "r", encoding="utf-8") as f:
            for linea in f:
                campos = linea.split(",") # la ultima parte tiene que ser el telefono
                if campos[0] == nombre:
                    print(f"Registro encontrado, {nombre} tien el telefono: {campos[1]}")
            print(f"No se ha encontrado el nombre {nombre}")
    else:
        raise FileNotFoundError ("[ERROR]: fichero contactos.txt no existe")