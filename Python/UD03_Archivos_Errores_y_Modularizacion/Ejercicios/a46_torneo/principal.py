"""
Actividad 46 — Paquete de inscripciones a un torneo. (Voluntaria)
Ejecutar desde esta carpeta: python principal.py
"""
import os
from torneo.inscripciones import inscribir, InscripcionError

ruta = "inscritos.txt"
# Borramos las pruebas de ejecuciones anteriores para empezar de cero
if os.path.exists(ruta):
    os.remove(ruta)

for jugador, nivel in [("Ana", "medio"), ("Luis", "experto"), ("Ana", "inicial"),
                       ("Eva", "pro"), ("Marta", "inicial")]:
    # Un unico except recoge tanto el duplicado como el nivel incorrecto
    try:
        inscribir(ruta, jugador, nivel)
        print(f"{jugador}: inscrito como {nivel}")
    except InscripcionError as error:
        print(f"{jugador}: rechazado -> {type(error).__name__}: {error}")

print("\nContenido de inscritos.txt:")
with open(ruta, "r", encoding="utf-8") as f:
    print(f.read())
