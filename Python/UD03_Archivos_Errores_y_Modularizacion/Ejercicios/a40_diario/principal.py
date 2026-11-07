# No sirve "from herramientas.diario import RUTA" y luego RUTA = "clase.txt": eso solo cambia la copia de
# este fichero; las funciones del modulo siguen usando SU propia RUTA (diario.txt). Hay que hacer diario.RUTA = ...
"""
Actividad 40 — Paquete de diario configurable con autotest. (Obligatoria)
Programa principal. Ejecutar desde esta carpeta: python principal.py
"""
import os
from herramientas import diario
from herramientas.diario import EntradaError

# Cambiamos el destino EN el modulo (diario.RUTA), asi sus funciones lo usan
diario.RUTA = "clase.txt"
if os.path.exists(diario.RUTA):
    os.remove(diario.RUTA)

entradas = ["Repaso de with", "                ",
            "Excepciones propias y jerarquías de errores", "Paquetes"]
for entrada in entradas:
    try:
        diario.apuntar(entrada)
        print(f"Apuntada: {entrada.strip()!r}")
    except EntradaError as e:
        print(f"[RECHAZADA]: {e}")

print("\nContenido de clase.txt:")
with open("clase.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Comprobamos que NO se ha creado el fichero por defecto
print("¿Se ha creado diario.txt?", os.path.exists("diario.txt"))
