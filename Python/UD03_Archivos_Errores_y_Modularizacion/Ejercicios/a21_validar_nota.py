"""
Actividad 21 — Validar nota de examen.
Escribe una función validar_nota_examen(nota) que lance 
un ValueError si la nota no está entre 0 y 10. Desde el programa 
principal, pide notas en un bucle hasta que el usuario escriba “fin”,
capturando el error en cada iteración sin que el bucle se detenga
"""
def validar_nota_examen(nota):
    if (0.0 <= nota <= 10.0):
        return nota
    else:
        raise ValueError("La nota debe estar entre 0 y 10!")

salir = False

while salir == False:
    try:
        entrada_nota_usuario = input("Introduce una nota: ")
        if entrada_nota_usuario == "fin":
            print("Saliendo")
            salir = True
            break
        else:
            nota = validar_nota_examen(float(entrada_nota_usuario))
            print(f"Nota válida: {nota}")
    except ValueError as e:
        print(f"[ERROR]: {e}")
        continue