"""
Actividad 24 — Validar archivo de configuración.
Crea un archivo configuracion.txt con líneas del tipo 
clave=valor. Escribe un programa que compruebe si están presentes 
todas las claves de una lista de claves obligatorias, avisando
(sin detener el programa) de cuáles faltan
"""
import os

fichero = "../output/configuracion.txt"
def verificar_claves(linea):
    campos = linea.split("=")
    campos = [c.replace('\n', '') for c in campos]
    if len(campos) != 2:
        raise ValueError("Cantidad de argumentos no validos")
    else:
        return campos

if os.path.exists(fichero):
    with open(fichero, "r", encoding="utf-8") as f:
        for linea in f:
            try:
                campos = verificar_claves(linea)
                print(f"Campos: {campos}")
            except ValueError as e:
                print(f"[ERROR]: {e} -> {linea}")
else:
    print("El archivo no existe. Crealo y agrega contenido siguiendo el patron correcto")
