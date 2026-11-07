"""
Actividad 23 — Registro de intentos de acceso.
Simula la introducción de una contraseña: cada vez que 
el valor introducido no coincida con la contraseña 
correcta, añade una línea al archivo intentos.log. Al tercer fallo consecutivo, el
programa debe avisar de que el acceso queda bloqueado.
"""
fichero_logs = "../output/intentos.log"

# Apuntamos el fallo en el log. NO guardamos lo que escribio el usuario:
# una contrasena en un fichero de texto seria un riesgo de seguridad.
def guardar_intento(numero_fallo):
    # Modo "a": anade al final (y crea el fichero si no existe).
    # El "\n" separa cada fallo en su propia linea (antes se pegaban todos).
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
# Si salimos del bucle con 3 fallos, bloqueamos el acceso
if contador == 3:
    print("Acceso bloqueado")
