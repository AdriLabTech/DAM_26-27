"""
Actividad 3. Acceso al cine con descuento
Pide la edad de una persona y si es estudiante (respuesta "si"/"no"). Tiene descuento si es
menor de 18 o si es estudiante, aunque tenga 18 o más. Escríbelo primero con una condición
compuesta (or) y después, en un comentario, explica cómo quedaría con if anidados
"""
# Capturamos la edad como entero y la respuesta del estudiante como texto.
# Guardamos la comparacion en una variable booleana, que vale True o False
edad_usuario = int(input("Introduzca su edad: "))
entrada_estudiante = input("¿Eres Estudiante? (si/no): ")
es_estudiante = entrada_estudiante == "si"

# El operador or junta las dos condiciones: el descuento se aplica si el
# usuario es menor de 18 O si es estudiante. Con que una de las dos sea True
# ya basta, no hace falta que las dos se cumplan
aplica_descuento = edad_usuario < 18 or es_estudiante

# Mostramos el resultado con una condicional ternaria
print("Se aplica el descunto!!!" if aplica_descuento else "No aplica descuento...")

# Usando if anidados quedaria asi: primero miramos si es menor de 18 y, solo si
# no lo es, comprobamos si es estudiante. Son menos lineas pero queda mas anidado
"""
if edad_usuario < 18:
    aplica_descuento = True
else:
    if es_estudiante:
        aplica_descuento = True
    else:
        aplica_descuento = False
"""