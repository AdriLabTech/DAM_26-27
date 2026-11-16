"""
Actividad 46 — Inscripciones a un torneo. Formato del fichero: jugador;nivel
"""
NIVELES = ("inicial", "medio", "experto")

class InscripcionError(Exception):
    pass

class DuplicadoError(InscripcionError):
    pass

class NivelError(InscripcionError):
    pass

def inscribir(ruta, jugador, nivel):
    if nivel not in NIVELES:
        raise NivelError(f"nivel no válido: {nivel!r}")
    # Miramos si el jugador ya esta inscrito
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.split(";")[0] == jugador:
                    raise DuplicadoError(jugador)
    except FileNotFoundError:
        # Sin fichero todavia no hay inscritos (el modo "a" lo creara).
        # DuplicadoError no es un FileNotFoundError, asi que sigue subiendo.
        pass
    with open(ruta, "a", encoding="utf-8") as f:
        f.write(f"{jugador};{nivel}\n")
