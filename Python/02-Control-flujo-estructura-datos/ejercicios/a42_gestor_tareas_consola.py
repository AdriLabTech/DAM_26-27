"""
Actividad 42 - Gestor de tareas en consola
Escribe un programa con un menú que se repita con while hasta que el usuario elija "Salir".
El menú debe ofrecer las siguientes opciones:
1. Añadir tarea: pide un texto y lo guarda en una lista de tareas, cada tarea
representada como un diccionario {"texto": ..., "hecha": False}.
2. Mostrar tareas: recorre la lista con for y enumerate(), mostrando cada tarea
numerada junto con su estado ("Pendiente" o "Hecha").
3. Completar tarea: pide el número de una tarea y cambia su clave "hecha" a True.
4. Salir: termina el bucle y el programa.
Debes estructurar al menos las opciones 1, 2 y 3 como funciones independientes, que
reciban la lista de tareas como parámetro. Comenta el código explicando la función de cada
parte
"""


def anadir_tarea(lista_tareas):
    """Crea una tarea y la anade al final de la lista."""
    nombre_tarea = input("Nombre de la tarea: ")

    # Cada tarea es un diccionario con el texto y su estado, que empieza
    # siempre como "Pendiente"
    tarea = {
        "nombre": nombre_tarea,
        "estado": "Pendiente"
    }

    # append() anade la tarea al final de la lista que nos han pasado
    lista_tareas.append(tarea)


def mostrar_tareas(lista_tareas):
    """Recorre la lista y muestra cada tarea numerada con su estado.
    # enumerate() devuelve el numero de posicion y la tarea a la vez, que es
    # justo lo que pide el enunciado para mostrarlas numeradas
    """
    for indice, tarea in enumerate(lista_tareas, start=1):
        print(f"Tarea {indice}: {tarea['nombre']} - {tarea['estado']}")


def completar_tarea(lista_tareas):
    """Pide el numero de una tarea y la marca como completada."""
    # El numero que escribe el usuario es la posicion, pero enumerate() empieza
    # en 1, asi que restamos 1 para convertirlo en indice real de la lista
    posicion = int(input("Ingresa el numero de la tarea: ")) - 1

    # Los diccionarios son mutables, asi que cambiamos el estado directamente
    lista_tareas[posicion]["estado"] = "Hecha"
    print("Tarea completada!")


def mostrar_opciones():
    """Muestra el menu y devuelve la opcion elegida por el usuario."""
    print("1 - Agregar tarea")
    print("2 - Mostrar todas las tareas")
    print("3 - Completar tarea")
    print("4 - Salir")

    # Devolvemos la opcion ya convertida a entero para compararla luego
    return int(input())


# La opcion se inicializa a 0 (distinta de 4) para que el while entre al menos
# una vez
opcion_usuario = 0
lista_tareas = []

while opcion_usuario != 4:
    opcion_usuario = mostrar_opciones()

    # match/case compara el valor con cada case. Se evaluan en orden y solo
    # entra en el que coincide
    match opcion_usuario:
        case 1:
            anadir_tarea(lista_tareas)
        case 2:
            mostrar_tareas(lista_tareas)
        case 3:
            completar_tarea(lista_tareas)
        case 4:
            # El break sale del while y termina el programa
            print("Saliendo...")
            break