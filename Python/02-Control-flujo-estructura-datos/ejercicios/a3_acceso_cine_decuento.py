"""
Actividad 3. Acceso al cine con descuento
Pide la edad de una persona y si es estudiante (respuesta "si"/"no"). Tiene descuento si es
menor de 18 o si es estudiante, aunque tenga 18 o más. Escríbelo primero con una condición
compuesta (or) y después, en un comentario, explica cómo quedaría con if anidados
"""
# Capturamos la entrada del usuario casteandola a entero
edad_usuario = int(input("Introduzca su edad: "))
entrada_estudiante = input("¿Eres Estudiante? (si/no): ")
es_estudiante = entrada_estudiante == "si"
aplica_descuento = edad_usuario < 18 or es_estudiante

# Mostramos resultados por pantalla
print("Se aplica el descunto!!!" if aplica_descuento else "No aplica descuento...")

# Usandos if anidados quedaria asi:
"""
aplica_descuento = False
if edad_usuario < 18:
    aplica_descuento = True
else:
    if es_estudiante:
        aplica_descuento = True
"""