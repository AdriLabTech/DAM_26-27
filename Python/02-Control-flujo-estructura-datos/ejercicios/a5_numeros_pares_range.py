"""
Actividad 5. Números pares con range con paso
Usando una sola llamada a range() con tres argumentos (inicio, fin, paso), muestra todos
los números pares entre 0 y 30 sin usar ningún if dentro del bucle.
"""
# El tercer argumento de range() es el paso. Con paso 2 el bucle avanza de dos en
# dos, asi que solo pasa por los numeros pares y no hace falta ningun if.
# El 31 queda fuera porque range() nunca llega al final
for i in range(0, 31, 2):
    print(i)