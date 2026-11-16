"""
Actividad 33 — Sistema de logging propio
registrar(nivel, mensaje): anade al fichero aplicacion.log una linea [INFO] mensaje
o [ERROR] mensaje segun el nivel.
"""
fichero_log = "../output/aplicacion.log"
NIVELES = ("INFO", "ERROR")

def registrar(nivel, mensaje):
    if nivel not in NIVELES:
        raise ValueError(f"nivel desconocido: {nivel!r}")
    with open(fichero_log, "a", encoding="utf-8") as f:
        f.write(f"[{nivel}] {mensaje}\n")
