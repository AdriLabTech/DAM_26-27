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

# Fichero main.py
from modulos import contactos

# Funcion 1.- Agregar contactos
contactos.añadir_contacto("Adrian","644-644-644")

print("Contactos")
# Funcion 2.- Listar contactos
contactos.listar_contactos()

# Funcion 3.- Buscar un contacto (no existente)
contactos.buscar_contacto("Rafa")

# Funcion 3.- Buscar un contacto exitente
contactos.buscar_contacto("Adrian")