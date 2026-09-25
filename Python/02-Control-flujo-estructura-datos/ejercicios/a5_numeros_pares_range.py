"""
Actividad 5. Números pares con range con paso
Usando una sola llamada a range() con tres argumentos (inicio, fin, paso), muestra todos
los números pares entre 0 y 30 sin usar ningún if dentro del bucle.
"""
for i in range(0,31, 2): # El paso que hacemos es avanzar de dos en dos (solo los pares)
    print(i)