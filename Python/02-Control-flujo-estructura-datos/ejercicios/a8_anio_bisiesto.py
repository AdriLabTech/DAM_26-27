"""
Actividad 8. Año bisiesto
Pide un año al usuario y determina si es bisiesto (divisible entre 4, salvo que sea divisible
entre 100 y no entre 400), usando una condición compuesta.
"""
# Guardamos la entrada del usuario casteandola a entero
entrada_anio = int(input("Introduce el anio: "))
print(f"El año {entrada_anio} es bisiesto" if (entrada_anio % 100 == 0 and entrada_anio % 400 == 0) or entrada_anio % 4 == 0 else f"El año {entrada_anio} NO es bisiesto")
