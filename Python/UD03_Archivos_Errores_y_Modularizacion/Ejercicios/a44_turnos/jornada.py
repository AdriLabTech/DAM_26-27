"""
Actividad 44 — Módulo de turnos con autotest. (Voluntaria)
Calcula el tiempo trabajado de cada fichaje. Ejecutar desde esta carpeta: python jornada.py
"""
import turnos

fichajes = [("08:00", "14:05"), ("15:00", "17:3"), ("16:00", "25:00"),
            ("9.00", "13:00"), ("17:30", "19:15")]

for entrada, salida in fichajes:
    try:
        inicio = turnos.a_minutos(entrada)
        fin = turnos.a_minutos(salida)
    except ValueError as error:
        print(f"{entrada} -> {salida}: descartado ({error})")
    else:
        print(f"{entrada} -> {salida}: trabajado {turnos.formatear(fin - inicio)}")

# "17:3" se acepta porque int("3") vale 3 y se lee como 17:03: el modulo solo
# exige que los minutos sean un numero entre 0 y 59, no que tengan 2 cifras.
