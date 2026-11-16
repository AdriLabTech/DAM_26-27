"""
Actividad 33 — Sistema de logging propio. (Voluntaria) Crea un módulo logger.py con una
función registrar(nivel, mensaje) que añada al archivo aplicacion.log líneas con el
formato [INFO] mensaje o [ERROR] mensaje según el nivel indicado. Úsala desde varias
partes de otro programa para registrar su actividad.
"""
from modulos.logger import registrar, fichero_log

registrar("INFO", "El programa ha arrancado")

def dividir(a, b):
    try:
        resultado = a / b
        registrar("INFO", f"Division correcta: {a} / {b} = {resultado}")
        return resultado
    except ZeroDivisionError:
        registrar("ERROR", f"Intento de dividir {a} entre 0")
        return None

dividir(10, 2)
dividir(5, 0)

# Un nivel que no existe tambien se registra, como error
try:
    registrar("AVISO", "este nivel no existe")
except ValueError as e:
    registrar("ERROR", f"Nivel incorrecto: {e}")

registrar("INFO", "El programa ha terminado")

with open(fichero_log, "r", encoding="utf-8") as f:
    print(f.read())
