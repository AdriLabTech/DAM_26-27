# Actividad 8. Calculadora de IMC (obligatoria)

peso_kg = float(input("Introduce tu peso en Kilogramos: "))
altura_metros = float(input("Introduce tu altura en metros: "))

# Aplicamos la formula
imc = (peso_kg / altura_metros) ** 2

# Mostramos el resultado
print(f"Tu indice de masa corporal es: {imc}")
