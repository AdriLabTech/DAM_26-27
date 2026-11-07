"""
Actividad 29 — Módulo de estadísticas
Funciones media(lista), mayor(lista) y menor(lista) para listas de números.
"""
# Modulo de estadisticas: solo contiene funciones, no pide ni muestra nada

# Si la lista esta vacia no hay media ni mayor ni menor: avisamos con un error
def _comprobar_no_vacia(lista):
    if len(lista) == 0:
        raise ValueError("La lista esta vacia")

# Suma todos los numeros y divide entre cuantos hay
def media(lista):
    _comprobar_no_vacia(lista)
    return sum(lista) / len(lista)

# Recorremos la lista guardando el numero mas grande que hemos visto hasta ahora
def mayor(lista):
    _comprobar_no_vacia(lista)
    resultado = lista[0]
    for numero in lista:
        if numero > resultado:
            resultado = numero
    return resultado

# Igual que mayor, pero guardando el mas pequeno
def menor(lista):
    _comprobar_no_vacia(lista)
    resultado = lista[0]
    for numero in lista:
        if numero < resultado:
            resultado = numero
    return resultado
