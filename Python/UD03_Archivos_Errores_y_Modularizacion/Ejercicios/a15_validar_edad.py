"""
Actividad 15 — Validar una edad
Escribe una función validar_edad(edad) que lance un 
ValueError si la edad es negativa o mayor de 120. 
Desde el programa principal, pide una edad al usuario, 
llama a la función dentro de un  try/except y muestra 
un mensaje adecuado si la edad no es válida
"""

# Si la edad esta fuera de rango, "lanzamos" un error con raise
def validar_edad(edad):
    if edad < 0 or edad > 120:
        raise ValueError("La edad no es válida!!!")

# Pedimos la edad al usuario (antes se probaban valores escritos a mano)
try:
    edad_usuario = int(input("Introduce tu edad: "))
    validar_edad(edad_usuario)
    print("Edad valida!!!")
# Cubre tanto "no es un numero" (int falla) como "fuera de rango" (la funcion falla)
except ValueError as e:
    print(f"[ERROR]: {e}")
