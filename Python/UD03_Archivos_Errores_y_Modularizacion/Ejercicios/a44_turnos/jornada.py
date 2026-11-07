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
        # El else solo se ejecuta si el try no dio ningun error
        print(f"{entrada} -> {salida}: trabajado {turnos.formatear(fin - inicio)}")

# ¿Por que "17:3" se acepta?  int("3") vale 3, asi que se lee como 17:03.
# El modulo no exige que los minutos tengan 2 cifras, solo que sean un numero entre 0 y 59.
