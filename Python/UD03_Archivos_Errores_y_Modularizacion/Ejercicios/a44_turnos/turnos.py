"""
Actividad 44 — Módulo de turnos con autotest.
"""
# Convierte "hh:mm" en minutos totales (08:30 -> 510)
def a_minutos(texto):
    partes = texto.split(":")
    # Tienen que salir exactamente dos trozos: horas y minutos
    if len(partes) != 2:
        raise ValueError(f"formato no válido: {texto!r}")
    try:
        horas, minutos = int(partes[0]), int(partes[1])
    except ValueError:
        raise ValueError(f"formato no válido: {texto!r}") from None
    if not (0 <= horas <= 23 and 0 <= minutos <= 59):
        raise ValueError(f"hora fuera de rango: {texto!r}")
    return horas * 60 + minutos

# Convierte minutos en "h:mm" (125 -> 2:05); los minutos siempre con 2 cifras
def formatear(minutos):
    return f"{minutos // 60}:{minutos % 60:02d}"

# Solo se ejecuta si lanzamos este fichero directamente, no cuando lo importan
if __name__ == "__main__":
    assert a_minutos("08:30") == 510
    assert formatear(125) == "2:05"
    print("turnos.py: autotest superado")
