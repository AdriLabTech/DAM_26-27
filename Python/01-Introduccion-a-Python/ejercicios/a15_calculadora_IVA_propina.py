# Actividad 15. Calculadora de precio con IVA y propina

precio_sin_iva = float(input("Introduce el precio del producto sin IVA: "))

precio_con_iva = precio_sin_iva + ((precio_sin_iva * 21) / 100)

# TODO: Preguntar a que se refiere "Se añade una propina expresada en tanto por ciento"

print(f"El precio con IVA es: {precio_con_iva}")
