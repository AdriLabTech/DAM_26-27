"""
Actividad 12. Contar vocales
Pide una palabra al usuario y cuenta, recorriendo sus letras con un bucle for y un
condicional, cuántas vocales contiene.
"""
# Capturamos la palabra. No hace falta convertirla porque solo vamos a recorrer
# sus caracteres tal cual
palabra = input("Introduce una palabra: ")

contador_vocales = 0

# Recorremos la palabra letra a letra. En un string, un for normal ya devuelve
# cada caracter por separado, no hace falta ir por los indices
for char in palabra:
    # El operador in devuelve True si el caracter esta dentro de la tupla de
    # vocales, y False si no. Asi no hace falta escribir cinco condiciones
    if char in ('a', 'e', 'i', 'o', 'u'):
        contador_vocales += 1

print(f"Cantidad de vocales: {contador_vocales}")