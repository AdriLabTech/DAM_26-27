"""
Actividad 31 — Módulo de fechas
validar_fecha_dd_mm_aaaa(texto): comprueba a mano (sin datetime) si el texto es una
fecha plausible con formato dd/mm/aaaa. Lanza ValueError si no lo es.
"""
# Bisiesto: divisible entre 4, y los de siglo solo si lo son entre 400
def _es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

def _dias_del_mes(mes, anio):
    if mes == 2:
        return 29 if _es_bisiesto(anio) else 28
    if mes in (4, 6, 9, 11):
        return 30
    return 31

def validar_fecha_dd_mm_aaaa(texto):
    partes = texto.split("/")
    if len(partes) != 3 or [len(p) for p in partes] != [2, 2, 4]:
        raise ValueError(f"formato no válido (usa dd/mm/aaaa): {texto!r}")
    dia, mes, anio = partes
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        raise ValueError(f"la fecha solo puede llevar números: {texto!r}")
    dia, mes, anio = int(dia), int(mes), int(anio)
    # Año plausible: entre 1900 y 2100
    if not 1900 <= anio <= 2100:
        raise ValueError(f"año fuera de rango: {texto!r}")
    if not 1 <= mes <= 12:
        raise ValueError(f"mes fuera de rango: {texto!r}")
    if not 1 <= dia <= _dias_del_mes(mes, anio):
        raise ValueError(f"día fuera de rango: {texto!r}")
    return dia, mes, anio
