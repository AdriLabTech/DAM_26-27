"""
Actividad 31 — Módulo de fechas. (Voluntaria) Crea un módulo fechas.py con una función
validar_fecha_dd_mm_aaaa(texto) que, sin usar el módulo datetime, compruebe manualmente
(formato y rangos de día/mes/año) si el texto recibido es una fecha plausible, lanzando
ValueError si no lo es. Pruébala desde un main.py con varios valores.
"""
from modulos import fechas

# Probamos fechas buenas y malas; cada una con su propio try/except
pruebas = ["07/11/2026", "29/02/2024", "29/02/2025", "31/04/2026",
           "15/13/2026", "1/1/2026", "ab/cd/efgh", "2026-11-07", "10/10/1850"]

for texto in pruebas:
    try:
        dia, mes, anio = fechas.validar_fecha_dd_mm_aaaa(texto)
        print(f"{texto!r}: fecha valida (dia {dia}, mes {mes}, año {anio})")
    except ValueError as e:
        print(f"{texto!r}: [ERROR] {e}")
