"""
Actividad 39 — Módulo de préstamos con jerarquía de excepciones.
Este modulo no imprime nada ni decide que hacer con los errores: solo los lanza.
"""
# Error "padre": capturando este se capturan todos los de prestamo
class PrestamoError(Exception):
    pass

class SinEjemplaresError(PrestamoError):
    pass

class LibroDesconocidoError(PrestamoError):
    pass

# DiasError hereda de ValueError porque unos dias malos son un valor malo
class DiasError(ValueError):
    pass

def prestar(catalogo, titulo, dias):
    if not 1 <= dias <= 30:
        raise DiasError(dias)
    # Si el libro no esta, traducimos el KeyError a un error nuestro
    try:
        ejemplares = catalogo[titulo]
    except KeyError as error:
        raise LibroDesconocidoError(f"no existe {titulo!r}") from error
    if ejemplares == 0:
        raise SinEjemplaresError(titulo)
    # Todo bien: descontamos un ejemplar y devolvemos los que quedan
    catalogo[titulo] = ejemplares - 1
    return catalogo[titulo]
