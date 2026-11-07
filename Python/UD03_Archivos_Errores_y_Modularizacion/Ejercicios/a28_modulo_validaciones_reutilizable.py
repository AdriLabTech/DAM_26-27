"""
Actividad 28 — Módulo de validaciones reutilizable. (Obligatoria) Crea un módulo
validaciones.py con una función validar_nota(nota) que lance un ValueError si la nota no
está entre 0 y 10. Desde un programa main.py, importa la función, pide notas al usuario
en un bucle hasta que escriba “fin”, y usa try/except para avisar (sin detener el programa)
cada vez que se introduzca una nota fuera de rango
"""
# Importamos nuestro modulo con la funcion validar_nota
from modulos import validaciones

while True:
    entrada_usuario = input("Introduce una nota: ")

    if entrada_usuario == "fin":
        break

    # El try esta dentro del bucle: un error avisa pero no detiene el programa
    try:
        n = float(entrada_usuario)
        if validaciones.validar_nota(n):
            print("Nota guardada con exito")
    except ValueError as e:
        print(f"[ERROR]: {e}")
