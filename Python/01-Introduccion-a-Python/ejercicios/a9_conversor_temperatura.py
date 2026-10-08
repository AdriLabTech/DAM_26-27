"""
# ---------------------------------------------------
# Actividad 9. Conversor de unidades de temperatura
# ---------------------------------------------------

Capturamos la entrada del usuario y la convertimos a float
"""
grados_celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Aplicamos la formula de conversion
grados_fahrenheit = (grados_celsius * (9 / 5)) + 32

print(f"La temperatura en grados Fahrenheit es: {round(grados_fahrenheit, 1)}")

