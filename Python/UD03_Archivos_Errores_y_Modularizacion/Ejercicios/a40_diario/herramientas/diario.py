"""
Actividad 40 — Diario configurable con autotest.
"""
import os

RUTA = "diario.txt"   # fichero donde se apuntan las entradas (se puede cambiar desde fuera)
MAXIMO = 30           # largo maximo de una entrada

class EntradaError(Exception):
    pass

# Deja el fichero vacio: abrirlo en modo "w" lo borra y al cerrarlo queda en blanco
def vaciar():
    with open(RUTA, "w", encoding="utf-8"):
        pass

# Anade una entrada numerada: "01. texto"
def apuntar(texto):
    texto = texto.strip()
    if texto == "" or len(texto) > MAXIMO:
        raise EntradaError(f"entrada no válida: {texto!r}")
    # Contamos las lineas que ya hay para saber que numero toca
    lineas = 0
    try:
        with open(RUTA, "r", encoding="utf-8") as f:
            lineas = len(f.readlines())
    except FileNotFoundError:
        pass  # Aun no existe: el modo "a" de abajo lo creara
    with open(RUTA, "a", encoding="utf-8") as f:
        f.write(f"{lineas + 1:02d}. {texto}\n")

# Este bloque solo se ejecuta si lanzamos ESTE fichero directamente (no al importarlo)
if __name__ == "__main__":
    RUTA = "prueba_diario.txt"
    vaciar()
    apuntar("uno")
    apuntar(" dos ")
    with open(RUTA, "r", encoding="utf-8") as f:
        assert f.readlines() == ["01. uno\n", "02. dos\n"]
    os.remove(RUTA)
    print("diario.py: autotest superado")
