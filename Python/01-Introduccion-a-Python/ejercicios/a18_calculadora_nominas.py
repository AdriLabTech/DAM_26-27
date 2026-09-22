# Actividad 18. Reto integrador: calculadora de nomina simplificada

# Pedimos el salario burto anual
salario_bruto_anual = float(input("Introduzca su salario bruto anual: "))

# Calculamos el salario bruto mensual
salario_bruto_mensual = salario_bruto_anual / 12

# Porcentajes de retenciones
retencion_irpf = 15
cotizacion_seguridad_social = 6.35

# Calculamos el importe de las retenciones
importe_irpf = (salario_bruto_mensual * retencion_irpf) / 100
importe_seguridad_social = (salario_bruto_mensual * cotizacion_seguridad_social) / 100

# Calculamos el salario neto restando los importes
salario_neto_mesual = salario_bruto_mensual - importe_irpf - importe_seguridad_social

# Mostramos el resumen
print("-" * 3 + " RESUMEN DE LA NOMINA " + "-" * 3)
print(f"Salario bruto anual: {round(salario_bruto_anual, 2)}")
print(f"Salario bruto mensual: {round(salario_bruto_mensual, 2)}")
print(f"Retencion IRPF (15%): {round(importe_irpf, 2)}")
print(f"Cotizacion Seguridad social (6,35): {round(importe_seguridad_social, 2)}")
print(f"Salario neto mensual: {round(salario_neto_mesual, 2)}")
