"""
Actividad 10 — Registro con contador de intento
Escribe un programa que, cada vez que se ejecuta una acción 
(por ejemplo, un intento de acceso simulado), añada una línea 
al archivo registro.txt indicando el número de intento, por
ejemplo "Intento 1: ...", incrementando el contador en cada nueva línea escrita.
"""
# importamos os para trabajar con ficheros
import os
path_fichero = "../output/registro.txt"
lista_intentos = []
contador = 1

def agregar_intento(lista, contador):
    if os.path.exists(path_fichero):
        with open (path_fichero, "w", encoding="utf-8") as archivo:
            for intento in lista:
                archivo.write(f"Intento {contador}:  {intento} \n")
                contador += 1
    else:
        with open (path_fichero, "w", encoding="utf-8"):
            agregar_intento(lista, contador)

def leer_fichero(fichero):
    if os.path.exists(fichero):
        with open(fichero, "r", encoding="utf-8") as fichero:
            print(fichero.read())

usuario_correcto = "user"
contrasenia_correcta = "1234"

entrada_usuario_nombre = "esto no cuenta"
entrada_usuario_contrasenia = "esto no cuenta"

while entrada_usuario_nombre != usuario_correcto or entrada_usuario_contrasenia != contrasenia_correcta:
    entrada_usuario_nombre = input("Introduce el nombre del usuario: ")
    entrada_usuario_contrasenia = input("Introduce la contrasenia del usuario: ")
    if entrada_usuario_nombre != usuario_correcto or entrada_usuario_contrasenia != contrasenia_correcta:
        lista_intentos.append(entrada_usuario_nombre + " | " + entrada_usuario_contrasenia)

agregar_intento(lista_intentos, contador)
leer_fichero(path_fichero)