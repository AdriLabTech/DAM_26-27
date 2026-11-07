"""
Actividad 39 — Módulo de préstamos con jerarquía de excepciones.
Este modulo no imprime nada ni decide que hacer con los errores: solo los lanza.
"""
# Error "padre" de los problemas de prestamo: asi se pueden capturar todos juntos
class PrestamoError(Exception):
    pass

class SinEjemplaresError(PrestamoError):
    pass

class LibroDesconocidoError(PrestamoError):
    pass

# DiasError hereda de ValueError (no de PrestamoError): un numero de dias malo es un valor malo
class DiasError(ValueError):
    pass

def prestar(catalogo, titulo, dias):
    # 1) Los dias tienen que estar entre 1 y 30
    if not 1 <= dias <= 30:
        raise DiasError(dias)
    # 2) Si el libro no esta en el catalogo, traducimos el KeyError a nuestro error
    try:
        ejemplares = catalogo[titulo]
    except KeyError as error:
        raise LibroDesconocidoError(f"no existe {titulo!r}") from error
    # 3) Sin ejemplares no se puede prestar
    if ejemplares == 0:
        raise SinEjemplaresError(titulo)
    # 4) Todo bien: descontamos un ejemplar y devolvemos los que quedan
    catalogo[titulo] = ejemplares - 1
    return catalogo[titulo]
