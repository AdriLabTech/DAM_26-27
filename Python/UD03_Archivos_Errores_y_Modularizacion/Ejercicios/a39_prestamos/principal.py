"""
Actividad 39 — Módulo de préstamos con jerarquía de excepciones. (Obligatoria)
Programa principal: decide que hacer con cada error. Ejecutar desde esta carpeta.
"""
from prestamos import prestar, PrestamoError, SinEjemplaresError

# Si int() falla avisamos y relanzamos el mismo error
def a_dias(texto):
    try:
        return int(texto)
    except ValueError:
        print(f"(aviso) {texto!r} no es un número de días")
        raise

catalogo = {"Dune": 1, "Dune (copia)": 1, "Ensayo": 0, "Quijote": 2}
solicitudes = [("Dune", "14"), ("Dune", "7"), ("Dune", "10"), ("Ensayo", "5"),
               ("Quijote", "45"), ("Quijote", "x"), ("Hamlet", "3")]

for titulo, texto in solicitudes:
    # El try de fuera recoge los rechazos que el de dentro no resuelve
    try:
        try:
            dias = a_dias(texto)
            quedan = prestar(catalogo, titulo, dias)
        except SinEjemplaresError:
            # Probamos con la copia (que tambien puede fallar)
            quedan = prestar(catalogo, titulo + " (copia)", dias)
            print(f"{titulo}: sin ejemplares, se presta la copia (quedan {quedan})")
        except ValueError as error:
            # Cubre el int() fallido y DiasError, que es un ValueError
            print(f"{titulo}: {type(error).__name__}: {error}")
        else:
            print(f"{titulo}: prestado ({texto} días), quedan {quedan}")
    except PrestamoError as error:
        print(f"{titulo}: rechazado -> {type(error).__name__}: {error}")
