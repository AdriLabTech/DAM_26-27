"""
Actividad 43 — Conversor de longitudes que traduce errores. (Voluntaria)
"""
# Metros que vale cada unidad
FACTORES = {"km": 1000, "m": 1, "cm": 0.01}

class ConversionError(Exception):
    pass

class UnidadError(ConversionError):
    pass

# Hereda de ValueError: un valor negativo es un valor malo
class ValorNegativoError(ValueError):
    pass

def convertir(valor, origen, destino):
    try:
        if valor < 0:
            raise ValorNegativoError(valor)
    except TypeError:
        # Comparar un texto con un numero da TypeError: avisamos y lo relanzamos
        print(f"(aviso) {valor!r} no es un número")
        raise
    try:
        # Pasamos a metros y de ahi a la unidad de destino
        return valor * FACTORES[origen] / FACTORES[destino]
    except KeyError as error:
        # Traducimos el KeyError a un error mas claro
        raise UnidadError(f"unidad desconocida: {error}") from error

pruebas = [(2.5, "km", "m"), (150, "cm", "m"), (3, "mi", "km"), (-4, "m", "cm"), ("7", "m", "cm")]

for valor, origen, destino in pruebas:
    try:
        resultado = convertir(valor, origen, destino)
        print(f"{valor} {origen} = {resultado:g} {destino}")
    # Los dos errores se tratan igual
    except (UnidadError, ValueError) as error:
        print(f"[ERROR] {type(error).__name__}: {error}")
    # Lo inesperado (aqui, el TypeError del texto)
    except Exception as error:
        print(f"[INESPERADO] {type(error).__name__}: {error}")
