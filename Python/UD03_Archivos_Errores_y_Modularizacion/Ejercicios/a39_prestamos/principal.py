"""
Actividad 39 — Módulo de préstamos con jerarquía de excepciones. (Obligatoria)
Programa principal: decide que hacer con cada error. Ejecutar desde esta carpeta.
"""
# Importamos la funcion y las excepciones que necesitamos en una sola linea
from prestamos import prestar, PrestamoError, SinEjemplaresError

# Convierte el texto en numero de dias; si falla avisa y vuelve a lanzar el MISMO error
def a_dias(texto):
    try:
        return int(texto)
    except ValueError:
        print(f"(aviso) {texto!r} no es un número de días")
        raise  # "raise" solo, sin nada mas, relanza el error original

catalogo = {"Dune": 1, "Dune (copia)": 1, "Ensayo": 0, "Quijote": 2}
solicitudes = [("Dune", "14"), ("Dune", "7"), ("Dune", "10"), ("Ensayo", "5"),
               ("Quijote", "45"), ("Quijote", "x"), ("Hamlet", "3")]

for titulo, texto in solicitudes:
    # try exterior: recoge los rechazos que el interior no resuelve
    try:
        # try interior: convierte los dias y presta
        try:
            dias = a_dias(texto)
            quedan = prestar(catalogo, titulo, dias)
        except SinEjemplaresError:
            # Intentamos recuperarnos prestando la copia (esto tambien puede fallar)
            quedan = prestar(catalogo, titulo + " (copia)", dias)
            print(f"{titulo}: sin ejemplares, se presta la copia (quedan {quedan})")
        except ValueError as error:
            # Recoge el int() fallido y tambien DiasError (que es un ValueError)
            print(f"{titulo}: {type(error).__name__}: {error}")
        else:
            print(f"{titulo}: prestado ({texto} días), quedan {quedan}")
    except PrestamoError as error:
        print(f"{titulo}: rechazado -> {type(error).__name__}: {error}")
