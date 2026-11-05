"""
Actividad 36 - Frecuencia de palabras
Dado un texto ya escrito en el código, cuenta con un diccionario cuántas veces aparece cada
palabra (recorriendo el texto con un bucle for), sin usar la clase Counter
"""
texto = "Esto es un texto para contar las veces que se repite cada palabra que se repite en un texto que es esto un texto que se repite en un texto que se repite"

# split() parte el texto en una lista de palabras usando los espacios como
# separador, asi que no hace falta recorrer el texto caracter a caracter
palabras = texto.split()

# El diccionario va a ser nuestro contador: la clave es la palabra y el valor
# cuantas veces ha aparecido
ocurrencias = {}

for palabra in palabras:
    # El operador in comprueba si la palabra ya tiene entrada en el diccionario
    if palabra in ocurrencias:
        # Si ya estaba, solo sumamos una unidad a su contador
        ocurrencias[palabra] += 1
    else:
        # Si es la primera vez que aparece, la creamos con valor 1
        ocurrencias[palabra] = 1

# items() devuelve cada par clave-valor del diccionario para poder mostrarlos
for palabra, cantidad in ocurrencias.items():
    print(f"Palabra: {palabra} | Contador: {cantidad}")