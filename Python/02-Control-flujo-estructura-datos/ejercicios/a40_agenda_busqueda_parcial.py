"""
Actividad 40 - Agenda con búsqueda parcial
Amplía la actividad de la agenda de contactos para que se pueda buscar un contacto
escribiendo solo una parte de su nombre, mostrando todos los contactos cuyo nombre la
contenga
"""


def buscar_alumnos(nombre_parcial):
    # Convertimos tambien lo que busca el usuario a minusculas, para que la
    # comparacion no dependa de si escribe "A" o "a"
    nombre_parcial = nombre_parcial.lower()

    for elemento in lista_alumnos:
        # __contains__() devuelve True si el nombre del alumno incluye el
        # texto buscado, que es lo que hace la busqueda parcial: no hace falta
        # que coincidan los nombres enteros
        if elemento["alumno"]["nombre"].lower().__contains__(nombre_parcial):
            print(f"ID_ALUMNO: {elemento['id_alumno']} | ALUMNO: {elemento['alumno']['nombre']} - NOTA: {elemento['alumno']['nota']}")


# Datos de los alumnos, con el diccionario anidado de la actividad anterior
alumno1 = {
    "id": "id_30-9-2026_17-29",
    "nombre": "Adrian"
}
notas_alumno1 = {
    "id": alumno1["id"],
    "nota": 10
}

diccionario_alumno1 = {
    "id_alumno": alumno1["id"],
    "alumno": {
        "nombre": alumno1["nombre"],
        "nota": notas_alumno1["nota"]
    }
}

alumno2 = {
    "id": "id_30-9-2026_17-42",
    "nombre": "Rafa"
}
notas_alumno2 = {
    "id": alumno2["id"],
    "nota": 6
}

diccionario_alumno2 = {
    "id_alumno": alumno2["id"],
    "alumno": {
        "nombre": alumno2["nombre"],
        "nota": notas_alumno2["nota"]
    }
}

lista_alumnos = []
lista_alumnos.append(diccionario_alumno1)
lista_alumnos.append(diccionario_alumno2)

# Probamos la busqueda con tres casos distintos
print("CASO 1")
buscar_alumnos("a")
print("CASO 2")
buscar_alumnos("r")
print("CASO 3")
buscar_alumnos("f")