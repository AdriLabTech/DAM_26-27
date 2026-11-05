"""
Actividad 18 — Validar un DNI simplificado.
Escribe una función validar_dni_simple(dni) que lance un ValueError
 si el DNI no tiene una longitud fija de 9 caracteres. Pruébala desde 
 el programa principal con varios valores, capturando el error con try/except
"""
def validar_dni_simple(dni):
    if len(dni) != 9:
        raise ValueError ("La longitud del DNI no es correcta")
    else:
        return "El DNI se ha guardado correctamente!"

try:
    print(validar_dni_simple("12312323Y"))
    print(validar_dni_simple("Este DNI no tiene 9 caracteres"))
    print(validar_dni_simple("hjkhjkhjk2")) # Como captura la excepcion, aqui no entra
except (ValueError) as e:
    print(f"[ERROR]: {e}")