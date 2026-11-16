"""
Actividad 42 — Serie con huecos: imputar el último valor válido. (Voluntaria)
Los valores que no se pueden convertir a numero se sustituyen por el ultimo valor bueno.
"""
valores = ["--", "20.0", "21.5", "--", "x", "19.35", ""]

ultimo = None     # ultimo valor valido
anterior = None   # ultimo valor mostrado, para calcular la variacion

for numero, texto in enumerate(valores, start=1):
    try:
        valor = float(texto)
        marca = "ok"
        ultimo = valor
    except ValueError:
        # Sin numero: usamos el ultimo bueno, y si aun no hay ninguno se descarta
        if ultimo is None:
            print(f"{numero}. {texto!r}: descartado (aun no hay valor anterior)")
            continue
        valor = ultimo
        marca = "imputado"

    # Desde el segundo valor mostramos tambien la variacion en %
    if anterior is None:
        print(f"{numero}. {valor:.2f} {marca}")
    else:
        variacion = (valor - anterior) / anterior * 100
        print(f"{numero}. {valor:.2f} {marca} ({variacion:+.1f} %)")
    anterior = valor
