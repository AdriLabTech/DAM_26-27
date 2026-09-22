# Actividad 17. Conversor de divisas con varias salidas

# Equivalencia 1:1 con respecto a otras monedas
valor_dolar = 1.15
valor_yuan = 7.69
valor_lempira = 30.80

euros_entrada = float(input("Introduce una cantidad en euros: "))

# Aplicamos directamente las conversiones
print(f"Conversion a Dolares: {round((valor_dolar * euros_entrada), 2)} dolares.")
print(f"Conversion a Yuanes: {round((valor_yuan * euros_entrada), 2)} yuanes.")
print(f"Conversion a Lempiras: {round((valor_lempira * euros_entrada), 2)} lempiras.")

