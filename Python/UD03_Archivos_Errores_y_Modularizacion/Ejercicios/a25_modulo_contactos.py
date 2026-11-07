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

# Fichero main.py: importamos nuestro modulo (carpeta modulos/, fichero contactos.py)
from modulos import contactos

# Menu que se repite hasta que el usuario elige salir
while True:
    print("\n1. Añadir contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Salir")
    opcion = input("Elige una opcion: ")

    # Cada opcion llama a una funcion del modulo
    # (salta un error si falta el fichero, si el contacto no existe o si el dato no vale)
    try:
        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Telefono: ")
            contactos.añadir_contacto(nombre, telefono)
        elif opcion == "2":
            contactos.listar_contactos()
        elif opcion == "3":
            contactos.buscar_contacto(input("Nombre a buscar: "))
        elif opcion == "4":
            print("Adios")
            break
        else:
            print("Opcion no valida")
    except (FileNotFoundError, contactos.ContactoNoEncontradoError, ValueError) as e:
        print(e)
