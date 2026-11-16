"""
Actividad 45 — Módulo precios.py rediseñado.
Los tres problemas del original (precios_mal.py):
 1) Al importarlo ya ejecuta cosas y escribe por pantalla ("precios_mal cargado", un precio...).
 2) Mezcla print con return: un fallo solo se ve en pantalla, quien llama no se entera.
 3) Devuelve -1 como "valor trampa": se puede sumar sin querer (-1 + 8.5 = 7.5, un precio falso)
    y el int() puede fallar con un error sin explicar.
"""
TARIFAS = {"normal": 8.5, "reducida": 6.0}

# Un solo error propio para todo lo que pueda fallar al calcular un precio
class PrecioError(Exception):
    pass

def precio(tarifa, entradas):
    if tarifa not in TARIFAS:
        raise PrecioError(f"tarifa desconocida: {tarifa!r}")
    try:
        cantidad = int(entradas)
    except ValueError:
        # Cambiamos el error de int() por uno mas claro
        raise PrecioError(f"número de entradas no válido: {entradas!r}") from None
    if cantidad <= 0:
        raise PrecioError(f"el número de entradas debe ser positivo: {cantidad}")
    return TARIFAS[tarifa] * cantidad

# Autotest: solo si lanzamos este fichero directamente
if __name__ == "__main__":
    assert precio("normal", 2) == 17.0
    assert precio("reducida", "3") == 18.0
    for tarifa, entradas in [("infantil", 1), ("normal", "dos"), ("normal", 0)]:
        try:
            precio(tarifa, entradas)
        except PrecioError:
            pass
        else:
            raise AssertionError(f"debia fallar: {tarifa}, {entradas}")
    print("precios.py: autotest superado")
