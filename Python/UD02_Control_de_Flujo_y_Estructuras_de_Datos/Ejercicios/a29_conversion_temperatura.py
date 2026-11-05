"""
Actividad 29 - Conversion de temperaturas
Escribe una función celsius_a_fahrenheit(temperaturas) que reciba una lista de
temperaturas en grados Celsius y devuelva una nueva lista con las conversiones a
Fahrenheit, usando un bucle o una comprensión de listas
"""


# La funcion recibe una lista y devuelve OTRA lista distinta
def celsius_a_fahrenheit(temperaturas):
    lista_conversion = []

    for temp in temperaturas:
        # Formula de Celsius a Fahrenheit: temp * (9/5) + 32
        conversion = (temp * (9 / 5)) + 32

        # round() redondea al segundo decimal para que no salgan numeros con
        # muchisimos decimales
        lista_conversion.append(round(conversion, 2))

    return lista_conversion


lista_celsius = [12, 15.5, 19, 123.8]
print(f"Lista de temperaturas convertidas: {celsius_a_fahrenheit(lista_celsius)}")