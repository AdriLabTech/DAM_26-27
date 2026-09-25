"""
Actividad 9. Nota con matices
Pide una nota numérica y clasifícala en “Sobresaliente” (9-10), “Notable” (7-8.99), “Bien”
(6-6.99), “Suficiente” (5-5.99) o “Insuficiente” (menos de 5), usando una cadena de
if/elif/else.
"""
# Capturamos la entrada del usuario casteandola a float
nota = float(input("Introduce una nota: "))

if nota < 0:
    print("Nota no valida")
elif nota < 5 and nota >= 0:
    print("Insuficiente")
elif nota < 6 :
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
elif nota <= 10:
    print("Sobresaliente")
else:
    print("Nota no valida") # Valoramos la posibilidad de que el usuario introduzca una nota invalida