"""
Actividad 19 - Suma y media de varios numeros
Escribe una función resumen(*numeros) que reciba cualquier cantidad de números (usando *args)
y devuelva, en una tupla, su suma y su media. Pruébala llamándola con distinta
cantidad de argumentos cada vez (por ejemplo, con 2, con 5 y con 0 números).
"""


# El asterisco delante de numeros es lo que convierte el parametro en *args:
# la funcion puede recibir cuantos numeros queramos y Python los mete juntos
# dentro de una tupla
def resumen(*numeros):
    suma = 0
    contador = 0

    for i in numeros:
        suma += i
        contador += 1

    # Si no se pasa ningun numero el contador se queda en 0 y dividir entre el
    # daria error, asi que ese caso lo cubrimos aparte
    if contador != 0:
        media = suma / contador
    else:
        media = "NO se puede dividir entre 0"

    # Los parentesis crean la tupla que pide el enunciado
    return (suma, media)


# La misma funcion con distinta cantidad de argumentos en cada llamada
matrix1 = resumen(10, 5)
matrix2 = resumen(2, 7, 10, 5, 1)
matrix3 = resumen()

print(f"{matrix1}")
print(f"{matrix2}")
print(f"{matrix3}")