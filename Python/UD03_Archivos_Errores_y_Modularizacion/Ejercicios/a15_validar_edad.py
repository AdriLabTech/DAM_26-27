"""
Actividad 15 — Validar una edad
Escribe una función validar_edad(edad) que lance un 
ValueError si la edad es negativa o mayor de 120. 
Desde el programa principal, pide una edad al usuario, 
llama a la función dentro de un  try/except y muestra 
un mensaje adecuado si la edad no es válida
"""
# Importamos os para trabajar con ficheros
import os

def validar_edad(edad):
    if edad < 0 or edad > 120:
        raise ValueError("La edad no es válida!!!")
print("Ejemplo 1")
try:
    resultado = validar_edad(19)
    print("Edad valida!!!")
except ValueError as e:
    print(f"[ERROR]: {e}")

print("Ejemplo 2")
try:
    resultado = validar_edad(-12)
    print("Edad valida!!!")
except ValueError as e:
    print(f"[ERROR]: {e}")