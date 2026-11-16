"""
Actividad 24 — Validar archivo de configuración.
Crea un archivo configuracion.txt con líneas del tipo 
clave=valor. Escribe un programa que compruebe si están presentes 
todas las claves de una lista de claves obligatorias, avisando
(sin detener el programa) de cuáles faltan
"""
import os

fichero = "../output/configuracion.txt"
# Claves que tienen que estar si o si
CLAVES_OBLIGATORIAS = ["clave1", "clave2", "clave3", "clave8"]

# Solo corta por el primer "=", asi un valor como "hola=hola" tambien es valido
def leer_clave(linea):
    campos = linea.strip().split("=", 1)
    if len(campos) != 2:
        raise ValueError("La linea no tiene formato clave=valor")
    return campos

claves_encontradas = []

if os.path.exists(fichero):
    with open(fichero, "r", encoding="utf-8") as f:
        for linea in f:
            try:
                clave, valor = leer_clave(linea)
                claves_encontradas.append(clave)
            except ValueError as e:
                print(f"[ERROR]: {e} -> {linea.strip()!r}")

    for clave in CLAVES_OBLIGATORIAS:
        if clave in claves_encontradas:
            print(f"Clave '{clave}' presente")
        else:
            print(f"[AVISO]: falta la clave obligatoria '{clave}'")
else:
    print("El archivo no existe. Crealo y agrega contenido siguiendo el patron correcto")
