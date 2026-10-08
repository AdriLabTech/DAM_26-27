"""
Actividad 37 - Ficha de alumno con tupla de notas
Crea un diccionario con las claves "nombre" y "notas", donde "notas" es una tupla con 3
notas del alumno. Calcula y muestra la media de esas notas
"""
nombre_alumno = input("Introduce el nombre del alumno: ")

# Primero recogemos las tres notas en una lista, porque las listas se pueden
# modificar y nos facilitate meter valores con append()
entradas_notas = []
for i in range(0, 3):
    entradas_notas.append(float(input("Introduce una de las nota del alumno: ")))

# Convertimos la lista en tupla con tuple(), porque el enunciado pide que las
# notas se guarden en una tupla y asi ya no se podran modificar
notas = tuple(entradas_notas)

alumno = {
    "nombre": nombre_alumno,
    "notas": notas
}

# sum() suma todos los numeros de la tupla y len() cuenta cuantos hay, asi que
# dividiendo uno entre otro obtenemos la media. Funciona igual que con listas
print(f"La media de las notas del alumno/a {alumno['nombre']} es: {sum(alumno['notas']) / len(alumno['notas'])}")