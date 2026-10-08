"""
Actividad 20 - Es Primo
Escribe una función es_primo(numero) que devuelva True si el número es primo y False en
caso contrario, usando un bucle for. Pide un número al usuario y muestra si es primo o no
llamando a la función
"""
def es_primo(numero):
    # 0 y 1 no son primos, y el bucle de abajo no llegaria a comprobarlo
    # (range(2, 0) y range(2, 1) no se repiten ninguna vez), asi que los
    # descartamos antes de empezar
    if numero < 2:
        return False

    # Probamos a dividirlo entre todos los posibles divisores. En cuanto
    # encontramos uno que da resto 0 ya sabemos que no es primo, asi que
    # salimos del bucle con return
    for i in range(2, numero):
        if numero % i == 0:
            return False

    # Si el bucle se recorre entero sin encontrar divisores, es primo
    return True

numero = int(input("Introduce un numero: "))
print("Es primo" if es_primo(numero) else "No es primo")