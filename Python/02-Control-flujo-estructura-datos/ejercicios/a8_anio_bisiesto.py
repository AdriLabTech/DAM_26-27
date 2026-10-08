"""
Actividad 8. Año bisiesto
Pide un año al usuario y determine si es bisiesto (divisible entre 4, salvo que sea divisible
entre 100 y no entre 400), usando una condición compuesta.
"""
# Capturamos el año como entero
entrada_anio = int(input("Introduce el anio: "))

# Condicion compuesta: un año es bisiesto si cumple una de estas dos reglas.
# O bien es multiplo de 4 y no de 100, o bien es multiplo de 400 a la vez
# (por eso el "and" va con el 100 y el 400 juntos en el primer par de parentesis).
# Todo metido en una condicional ternaria dentro del print() para que el
# programa elija el mensaje correcto en una sola linea
print(
    f"El año {entrada_anio} es bisiesto"
    if (entrada_anio % 100 == 0 and entrada_anio % 400 == 0) or entrada_anio % 4 == 0
    else f"El año {entrada_anio} NO es bisiesto"
)