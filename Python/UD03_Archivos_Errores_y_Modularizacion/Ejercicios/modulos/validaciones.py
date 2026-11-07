"""
Actividad 28 — Módulo de validaciones reutilizable. (Obligatoria) Crea un módulo
validaciones.py con una función validar_nota(nota) que lance un ValueError si la nota no
está entre 0 y 10. Desde un programa main.py, importa la función, pide notas al usuario
en un bucle hasta que escriba “fin”, y usa try/except para avisar (sin detener el programa)
cada vez que se introduzca una nota fuera de rango
"""
# Modulo validaciones

def validar_nota(nota):
    # Antes estaba "0.0 < nota > 10.0", que no comprobaba bien el rango
    # (dejaba pasar notas negativas). Lo correcto: fuera de 0..10 -> error.
    if nota < 0.0 or nota > 10.0:
        raise ValueError("La nota debe estar comprendida entre 0 y 10")
    return True
