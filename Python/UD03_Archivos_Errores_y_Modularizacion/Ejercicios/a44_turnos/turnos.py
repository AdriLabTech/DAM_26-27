"""
Actividad 44 — Módulo de turnos con autotest.
"""
# "08:30" -> 510 minutos
def a_minutos(texto):
    partes = texto.split(":")
    if len(partes) != 2:
        raise ValueError(f"formato no válido: {texto!r}")
    try:
        horas, minutos = int(partes[0]), int(partes[1])
    except ValueError:
        raise ValueError(f"formato no válido: {texto!r}") from None
    if not (0 <= horas <= 23 and 0 <= minutos <= 59):
        raise ValueError(f"hora fuera de rango: {texto!r}")
    return horas * 60 + minutos

# 125 minutos -> "2:05"
def formatear(minutos):
    return f"{minutos // 60}:{minutos % 60:02d}"

# Autotest: solo si lanzamos este fichero directamente
if __name__ == "__main__":
    assert a_minutos("08:30") == 510
    assert formatear(125) == "2:05"
    print("turnos.py: autotest superado")
