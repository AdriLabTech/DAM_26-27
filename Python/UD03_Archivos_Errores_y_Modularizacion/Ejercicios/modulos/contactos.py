"""
Actividades 25, 34 y 35 — Módulo de contactos
Funciones: añadir_contacto, listar_contactos, buscar_contacto y eliminar_contacto.
Los contactos se guardan en contactos.txt, una linea por contacto: nombre,telefono
"""
import os
fichero_contactos = "../output/contactos.txt"

# Error propio: se lanza cuando se busca o elimina un contacto que no existe (actividad 34)
class ContactoNoEncontradoError(Exception):
    pass

# Lee todos los contactos del fichero y los devuelve como lista de (nombre, telefono)
def _leer_todos():
    if not os.path.exists(fichero_contactos):
        raise FileNotFoundError("el fichero contactos.txt no existe todavia")
    contactos = []
    with open(fichero_contactos, "r", encoding="utf-8") as f:
        for linea in f:
            if linea.strip() == "":
                continue
            nombre, telefono = linea.strip().split(",", 1)
            contactos.append((nombre, telefono))
    return contactos

def añadir_contacto(nombre, telefono):
    # La coma separa nombre y telefono en el fichero, asi que no puede ir dentro de ellos
    if "," in nombre or "," in telefono or nombre.strip() == "":
        raise ValueError("el nombre no puede estar vacio y ni nombre ni telefono pueden llevar comas")
    # Modo "a": anade al final del fichero sin borrar los contactos anteriores
    with open(fichero_contactos, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{telefono}\n")
    print("Registro guardado")

def listar_contactos():
    for nombre, telefono in _leer_todos():
        print("-----------------------------------")
        print(f"Registro: {nombre} -> {telefono}")
        print("-----------------------------------")

def buscar_contacto(nombre):
    for nombre_guardado, telefono in _leer_todos():
        if nombre_guardado == nombre:
            print(f"Registro encontrado, {nombre} tiene el telefono: {telefono}")
            return telefono
    # Solo llegamos aqui si no estaba en ninguna linea
    raise ContactoNoEncontradoError(f"No se ha encontrado el nombre {nombre}")

# Borra un contacto reescribiendo el fichero con todos los demas
def eliminar_contacto(nombre):
    contactos = _leer_todos()
    restantes = [c for c in contactos if c[0] != nombre]
    if len(restantes) == len(contactos):
        raise ContactoNoEncontradoError(f"No se ha encontrado el nombre {nombre}")
    with open(fichero_contactos, "w", encoding="utf-8") as f:
        for n, t in restantes:
            f.write(f"{n},{t}\n")
    print(f"Contacto {nombre} eliminado")
