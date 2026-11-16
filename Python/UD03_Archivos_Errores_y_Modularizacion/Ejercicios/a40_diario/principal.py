"""
Actividad 40 — Paquete de diario configurable con autotest. (Obligatoria)
Programa principal. Ejecutar desde esta carpeta: python principal.py
"""
import os
from herramientas import diario
from herramientas.diario import EntradaError

# Hay que cambiar la ruta en el propio modulo (diario.RUTA): con "from ... import RUTA"
# solo cambiaria una copia local y las funciones seguirian usando diario.txt
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

# El fichero por defecto no deberia haberse creado
print("¿Se ha creado diario.txt?", os.path.exists("diario.txt"))
