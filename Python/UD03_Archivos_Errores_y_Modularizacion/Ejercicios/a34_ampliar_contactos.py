"""
Actividad 34 — Ampliar el módulo de contactos. (Voluntaria) Amplía el módulo contactos.py
de la actividad 25 con una función eliminar_contacto(nombre) y una excepción propia
ContactoNoEncontradoError, que debe lanzarse cuando se intenta buscar o eliminar un
contacto que no existe.
"""
from modulos import contactos

# Preparamos dos contactos de prueba
contactos.añadir_contacto("Laura", "611-111-111")
contactos.añadir_contacto("Pedro", "622-222-222")

# Cada prueba lleva su try/except: asi vemos el error propio sin que el programa se pare
print("\n-- Buscar un contacto que existe --")
contactos.buscar_contacto("Laura")

print("\n-- Buscar un contacto que NO existe --")
try:
    contactos.buscar_contacto("Nadie")
except contactos.ContactoNoEncontradoError as e:
    print(f"[ERROR]: {e}")

print("\n-- Eliminar un contacto que existe --")
contactos.eliminar_contacto("Laura")

print("\n-- Eliminar un contacto que NO existe --")
try:
    contactos.eliminar_contacto("Laura")
except contactos.ContactoNoEncontradoError as e:
    print(f"[ERROR]: {e}")

print("\n-- Lista final --")
contactos.listar_contactos()
