"""
Actividad 18 — Validar un DNI simplificado.
Escribe una función validar_dni_simple(dni) que lance un ValueError
 si el DNI no tiene una longitud fija de 9 caracteres. Pruébala desde 
 el programa principal con varios valores, capturando el error con try/except
"""
# Un DNI correcto tiene exactamente 9 caracteres; si no, lanzamos error
def validar_dni_simple(dni):
    if len(dni) != 9:
        raise ValueError("La longitud del DNI no es correcta")
    return "El DNI se ha guardado correctamente!"

# Probamos varios valores. Cada uno lleva su propio try/except: asi un fallo
# no impide probar los siguientes (antes el segundo valor cortaba el programa)
for dni_prueba in ["12312323Y", "Este DNI no tiene 9 caracteres", "hjkhjkhjk2", "98765432A"]:
    try:
        print(f"{dni_prueba!r}: {validar_dni_simple(dni_prueba)}")
    except ValueError as e:
        print(f"{dni_prueba!r}: [ERROR]: {e}")
