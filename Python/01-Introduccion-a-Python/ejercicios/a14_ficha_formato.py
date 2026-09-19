# Actividad 14. Ficha de alumno con formato

nombre_usuario = input("Introduce tu nombre: ")
edad_usuario = int(input("Introduce tu edad: "))
nota_media_usuario = float(input("Introduce tu nota media del curso anterior: "))

# Mostrar la informacion con el formato exacto
print("-" * 3 + " FICHA DE ALUMNO " + "-" * 3)
print(f"Nombre: {nombre_usuario}")
print(f"Edad: {edad_usuario} años")
print(f"Nota media anterior: {round(nota_media_usuario, 2)}")

