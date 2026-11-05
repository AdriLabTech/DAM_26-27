"""
Actividad 35 - Consulta segura de un diccionario
Usando el diccionario alumno = {"nombre": "Ana", "edad": 18, "nota": 8.5}, pide al
usuario el nombre de una clave por teclado (por ejemplo, podría escribir "telefono", que
no existe) y muestra su valor usando .get() con un valor por defecto "Dato no disponible",
de forma que el programa nunca produzca un error aunque la clave no exista
"""
alumno = {
    "nombre": "Ana",
    "edad": 18,
    "nota": 8.5
}

# .get() es la alternativa segura a los corchetes: si la clave existe devuelve su
# valor y si no existe devuelve el segundo argumento que le pasamos. Aqui
# consultamos "telefono", que no esta en el diccionario, asi que en vez de
# lanzar un KeyError devuelve el texto por defecto
print(f"Telefono del alumno: {alumno.get('telefono', 'Dato no disponible')}")