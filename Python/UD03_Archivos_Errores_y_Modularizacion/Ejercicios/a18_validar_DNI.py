"""
Actividad 18 — Validar un DNI simplificado.
Escribe una función validar_dni_simple(dni) que lance un ValueError
 si el DNI no tiene una longitud fija de 9 caracteres. Pruébala desde 
 el programa principal con varios valores, capturando el error con try/except
"""
def validar_dni_simple(dni):
    if len(dni) != 9:
        raise ValueError("La longitud del DNI no es correcta")
    return "El DNI se ha guardado correctamente!"

# El try/except va dentro del bucle para que un fallo no corte las pruebas siguientes
for dni_prueba in ["12312323Y", "Este DNI no tiene 9 caracteres", "hjkhjkhjk2", "98765432A"]:
    try:
        print(f"{dni_prueba!r}: {validar_dni_simple(dni_prueba)}")
    except ValueError as e:
        print(f"{dni_prueba!r}: [ERROR]: {e}")
