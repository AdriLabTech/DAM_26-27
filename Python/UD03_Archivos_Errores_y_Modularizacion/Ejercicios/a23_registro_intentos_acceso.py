"""
Actividad 23 — Registro de intentos de acceso.
Simula la introducción de una contraseña: cada vez que 
el valor introducido no coincida con la contraseña 
correcta, añade una línea al archivo intentos.log. Al tercer fallo consecutivo, el
programa debe avisar de que el acceso queda bloqueado.
"""
fichero_logs = "../output/intentos.log"

# Solo apuntamos el numero de fallo, no lo que escribio el usuario:
# guardar contraseñas en un fichero de texto seria un riesgo
def guardar_intento(numero_fallo):
    with open(fichero_logs, "a", encoding="utf-8") as f:
        f.write(f"Intento fallido numero {numero_fallo}\n")

contrasenia_correcta = "contraseña_segura"
contador = 0
while contador != 3:
    entrada_usuario = input("Introduce la contraseña para acceder: ")
    if entrada_usuario == contrasenia_correcta:
        print("Acceso Concedido!!!")
        break
    contador += 1
    guardar_intento(contador)
# Si salimos del bucle con 3 fallos, se bloquea el acceso
if contador == 3:
    print("Acceso bloqueado")
