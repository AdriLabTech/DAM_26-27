"""
# -----------------------------------
# Actividad 13. Depuración de tipos.
# -----------------------------------
Capturamos la entrada del usuario y la convertimos a float
"""
precio_texto = float(input("Precio del artículo: ")) # La correccion esta en castear la entrada del usuario para poder operar con ella
descuento = 10
precio_final = precio_texto - descuento
print("El precio final es:", precio_final)
