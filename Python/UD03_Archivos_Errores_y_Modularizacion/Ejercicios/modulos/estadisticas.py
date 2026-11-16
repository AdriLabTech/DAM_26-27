"""
Actividad 29 — Módulo de estadísticas
Funciones media(lista), mayor(lista) y menor(lista) para listas de números.
"""
# Con la lista vacia no hay media, mayor ni menor
def _comprobar_no_vacia(lista):
    if len(lista) == 0:
        raise ValueError("La lista esta vacia")

def media(lista):
    _comprobar_no_vacia(lista)
    return sum(lista) / len(lista)

def mayor(lista):
    _comprobar_no_vacia(lista)
    return max(lista)

def menor(lista):
    _comprobar_no_vacia(lista)
    return min(lista)
