"""
Actividad 10 — Registro con contador de intento
Escribe un programa que, cada vez que se ejecuta una acción 
(por ejemplo, un intento de acceso simulado), añada una línea 
al archivo registro.txt indicando el número de intento, por
ejemplo "Intento 1: ...", incrementando el contador en cada nueva línea escrita.
"""
import os

path_fichero = "../output/registro.txt"

# Cada linea del registro es un intento, asi que contamos lineas para seguir por donde iba
def contar_intentos_previos():
    if not os.path.exists(path_fichero):
        return 0
    with open(path_fichero, "r", encoding="utf-8") as archivo:
        return len(archivo.readlines())

def agregar_intentos(lista):
    contador = contar_intentos_previos() + 1
    # Modo "a": añade al final sin borrar lo anterior
    with open(path_fichero, "a", encoding="utf-8") as archivo:
        for intento in lista:
            archivo.write(f"Intento {contador}: {intento}\n")
            contador += 1

usuario_correcto = "user"
contrasenia_correcta = "1234"

intentos_fallidos = []
acierto = False

while not acierto:
    nombre = input("Introduce el nombre del usuario: ")
    contrasenia = input("Introduce la contrasenia del usuario: ")
    if nombre == usuario_correcto and contrasenia == contrasenia_correcta:
        acierto = True
    else:
        intentos_fallidos.append(f"{nombre} | {contrasenia}")

agregar_intentos(intentos_fallidos)

with open(path_fichero, "r", encoding="utf-8") as archivo:
    print(archivo.read())
