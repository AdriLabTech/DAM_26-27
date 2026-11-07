"""
Actividad 33 — Sistema de logging propio
registrar(nivel, mensaje): anade al fichero aplicacion.log una linea [INFO] mensaje
o [ERROR] mensaje segun el nivel.
"""
fichero_log = "../output/aplicacion.log"
NIVELES = ("INFO", "ERROR")

def registrar(nivel, mensaje):
    # Solo aceptamos los niveles permitidos
    if nivel not in NIVELES:
        raise ValueError(f"nivel desconocido: {nivel!r}")
    # Modo "a": cada llamada anade una linea al final sin borrar las anteriores
    with open(fichero_log, "a", encoding="utf-8") as f:
        f.write(f"[{nivel}] {mensaje}\n")
