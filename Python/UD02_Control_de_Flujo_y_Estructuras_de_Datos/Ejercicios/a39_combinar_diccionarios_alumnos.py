"""
Actividad 39 - Combinar dos diccionarios de alumnos
Dado un diccionario de nombres de alumnos (id → nombre) y otro de sus notas (mismo id
→ nota), combínalos en un único diccionario id → {"nombre": …, "nota": …} para cada
alumno
"""
# Cada alumno tiene su propio diccionario de datos
alumno1 = {
    "id": "id_30-9-2026_17-29",
    "nombre": "Adrián"
}
notas_alumno1 = {
    "id": alumno1["id"],
    "nota": 10
}

# Unimos el nombre y la nota en un diccionario dentro de otro, que es el
# diccionario anidado que pide el enunciado
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

# Guardamos los dos alumnos en una lista para poder recorrerlos juntos
lista_alumnos = []
lista_alumnos.append(diccionario_alumno1)
lista_alumnos.append(diccionario_alumno2)

# Al ser el diccionario anidado hay que subir dos niveles para llegar a los
# datos: primero a elemento["alumno"] y despues a la clave concreta
for elemento in lista_alumnos:
    print(f"ID_ALUMNO: {elemento['id_alumno']} | ALUMNO: {elemento['alumno']['nombre']} - NOTA: {elemento['alumno']['nota']}")