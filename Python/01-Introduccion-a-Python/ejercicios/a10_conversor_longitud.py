# Actividad 10. Conversor de unidades de longitud

distancia_km = float(input("Ingresa la longitud en kilómetros: "))

distancia_metros = distancia_km * 1000

distancia_millas = distancia_km * 0.621371

distancia_millas_nauticas = distancia_km * 0.539957

print(f"Conversión a Metros: {round(distancia_metros, 3)}")

print(f"Conversión a Millas: {round(distancia_millas, 3)}")

print(f"Conversión de Millas Náuticas: {round(distancia_millas_nauticas, 3)}")
