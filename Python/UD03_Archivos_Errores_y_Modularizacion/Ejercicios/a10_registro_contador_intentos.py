"""
Actividad 10 — Registro con contador de intento
Escribe un programa que, cada vez que se ejecuta una acción 
(por ejemplo, un intento de acceso simulado), añada una línea 
al archivo registro.txt indicando el número de intento, por
ejemplo "Intento 1: ...", incrementando el contador en cada nueva línea escrita.
"""
# Importamos os para comprobar si el fichero existe
import os
path_fichero = "../output/registro.txt"

# Cuenta cuantas lineas tiene ya el registro, para seguir numerando desde ahi
def contar_intentos_previos():
    if os.path.exists(path_fichero):
        with open(path_fichero, "r", encoding="utf-8") as archivo:
            return len(archivo.readlines())
    return 0

# Anade los intentos fallidos al final del fichero
def agregar_intento(lista):
    contador = contar_intentos_previos() + 1
    # Modo "a": anade al final sin borrar lo anterior (y crea el fichero si no existe)
    with open(path_fichero, "a", encoding="utf-8") as archivo:
        for intento in lista:
            archivo.write(f"Intento {contador}:  {intento} \n")
            contador += 1

def leer_fichero(fichero):
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as archivo:
            print(archivo.read())

usuario_correcto = "user"
contrasenia_correcta = "1234"

lista_intentos = []
acierto = False

# Seguimos pidiendo datos hasta que acierte usuario y contrasenia
while not acierto:
    entrada_usuario_nombre = input("Introduce el nombre del usuario: ")
    entrada_usuario_contrasenia = input("Introduce la contrasenia del usuario: ")
    if entrada_usuario_nombre == usuario_correcto and entrada_usuario_contrasenia == contrasenia_correcta:
        acierto = True
    else:
        # Apuntamos el intento fallido para guardarlo despues
        lista_intentos.append(entrada_usuario_nombre + " | " + entrada_usuario_contrasenia)

agregar_intento(lista_intentos)
leer_fichero(path_fichero)
