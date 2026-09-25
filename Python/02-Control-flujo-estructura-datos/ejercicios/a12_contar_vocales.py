"""
Actividad 12. Contar vocales
Pide una palabra al usuario y cuenta, recorriendo sus letras con un bucle for y un
condicional, cuántas vocales contiene.
"""
# Capturamos la entrada del usuario
palabra = input("Introduce una palabra: ")

contador_vocales = 0
for char in palabra:
    if char in ('a', 'e', 'i', 'o', 'u'): # Defino el conjunto de vocales
        contador_vocales += 1
print(f"Cantidad de vocales: {contador_vocales}")