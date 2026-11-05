"""
Actividad 23 — Registro de intentos de acceso.
Simula la introducción de una contraseña: cada vez que 
el valor introducido no coincida con la contraseña 
correcta, añade una línea al archivo intentos.log. Al tercer fallo consecutivo, el
programa debe avisar de que el acceso queda bloqueado.
"""
import os

fichero_logs = "../output/intentos.log"

def guardar_intento(contrasenia):
    if os.path.exists(fichero_logs):
        with open(fichero_logs, "a", encoding="utf-8") as f:
            f.write(contrasenia)
    else:
        with open(fichero_logs, "w", encoding="utf-8"):
            guardar_intento(contrasenia)

contrasenia_correcta = "contraseña_segura"
contador = 0
while contador != 3:
    entrada_usuario = input("Introduce la contraseña para acceder: ")
    if entrada_usuario == contrasenia_correcta:
        print("Acceso Concedido!!!")
        break
    else:
        guardar_intento(entrada_usuario)
        contador += 1
if contador == 3:
    print("Acceso bloqueado")