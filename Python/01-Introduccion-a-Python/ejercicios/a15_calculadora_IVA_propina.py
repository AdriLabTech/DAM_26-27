# Actividad 15. Calculadora de precio con IVA y propina

precio_sin_iva = float(input("Introduce el precio del producto sin IVA: "))

precio_con_iva = precio_sin_iva + ((precio_sin_iva * 21) / 100)

# Pedimos una propina en tanto por ciento
propina = float(input("Agradeceriamos una propina en tanto por ciento. Cuanto por ciento quieres abonar?: "))

precio_propina = precio_con_iva + ((precio_con_iva * propina) / 100)

print(f"Precio sin IVA: {round(precio_sin_iva, 2)}")
print(f"Precio con IVA: {round(precio_con_iva,2)}")
print(f"Precio con IVA + Propina: {round(precio_propina, 2)}")
