# Actividad 19(reto). Calculadora de distancia entre dos puntos

# Pedimos la primera coordenada (x1 ,y1)
x1 = float(input("Introduce el valor X de la primera coordenada: "))
y1 = float(input("Introduce el valor Y de la primera coordenada: "))

# Pedimos la segunda coordenada (x2, y2)
x2 = float(input("Introduce el valor X de la segunda coordenada: "))
y2 = float(input("Introduce el valor Y de la segunda coordenada: "))

# Aplicamos la formula euclidea parar calcular la distancia entre dos puntos
distancia = ((x2 - x1)** 2 + (y2 - y1)** 2) ** 0.5

# Mostramos el resultado con 3 decimales u un texto adicion usando operadores de comparacion
print(f"Distancia Euclidea entre los dos puntos: {round(distancia, 3)} | " + ("La distancia es mayor a 10" if distancia > 10.0 else "La distancia es menor a 10"))

