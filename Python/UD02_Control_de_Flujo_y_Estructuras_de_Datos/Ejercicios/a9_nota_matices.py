"""
Actividad 9. Nota con matices
Pide una nota numérica y clasifícala en “Sobresaliente” (9-10), “Notable” (7-8.99), “Bien”
(6-6.99), “Suficiente” (5-5.99) o “Insuficiente” (menos de 5), usando una cadena de
if/elif/else.
"""
# Capturamos la nota como float, no como int, para poder meter decimales (7.5, 8.99...)
nota = float(input("Introduce una nota: "))

# Las condiciones van en orden ASCENDENTE y cada una solo comprueba el limite
# superior. El primero que se cumple gana, asi que al llegar a "nota < 5" ya
# sabemos que la nota es >= 0 y no hace falta volver a comprobarlo
if nota < 0:
    print("Nota no valida")
elif nota < 5:
    print("Insuficiente")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
elif nota <= 10:
    # Aqui si hay que comprobar <= 10, porque es el unico sitio donde el valor
    # 10 exacto tiene que entrar
    print("Sobresaliente")
else:
    # Si es mayor que 10 la nota no es valida
    print("Nota no valida")