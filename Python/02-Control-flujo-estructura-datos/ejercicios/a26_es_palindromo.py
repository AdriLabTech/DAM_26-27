"""
Actividad 26 - Es palindromo
Escribe una función es_palindromo(palabra) que devuelva True si la palabra se lee igual del
derecho que del revés. Pruébala con varias palabras desde el programa principal
"""


def es_palindromo(palabra):
    # Antes de comparar hay que NORMALIZAR la palabra. Con lower() la pasamos a
    # minusculas (si no, "Reconocer" y "reconocer" darian False) y con
    # replace() quitamos los espacios (si no, ninguna frase con espacios seria
    # palindromo)
    palabra = palabra.lower().replace(" ", "")

    # reversed() da la cadena del reves y join() la vuelve a unir en una sola
    # cadena, porque reversed entrega los caracteres sueltos
    palabra_invertida = "".join(reversed(palabra))

    return palabra == palabra_invertida


# Probamos con una palabra normal, una con mayusculas y una frase con espacios
print(f"La palabra hola es palindromo?: {es_palindromo('hola')}")
print(f"La palabra Reconocer es palindromo?: {es_palindromo('Reconocer')}")
print(f"La frase 'Somos o no somos' es palindromo?: {es_palindromo('Somos o no somos')}")