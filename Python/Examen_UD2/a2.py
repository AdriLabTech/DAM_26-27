"""
Un centro de salud atiende por prioridad: primero los de prioridad 1, luego 2 y 
por último 3; a igual prioridad, por orden de llegada. La cola es una lista de 
tuplas (nombre, prioridad, minutos), donde minutos es la duración de la 
consulta (0 indica que el paciente no se ha presentado). Datos de 
partida (cópialos tal cual):

cola = [("Lucía", 3, 15), ("Mario", 2, 20), ("Irene", 1, 30), ("Pablo", 3, 0),
        ("Sara", 2, 25), ("Hugo", 1, 10), ("Nora", 3, 20)]

Escribe una función siguiente(cola) que devuelva la posición 
del paciente que debe atenderse ahora: el de menor número de prioridad y, 
en caso de empate, el que va antes en la lista. No se permite usar min() ni max().
Escribe una función reclasificar(cola, *nombres) que, usando *args, 
suba a prioridad 1 a los pacientes indicados y devuelva cuántos ha 
reclasificado (los nombres que no estén en la cola se ignoran). Como las 
tuplas no se pueden modificar, cada tupla se sustituye por otra nueva en 
la misma posición: inserta la nueva con insert() y elimina la vieja con remove().
Escribe una función atender(cola, jornada=240) que, con un bucle while 
mientras queden pacientes, elija al siguiente con siguiente; si no se 
ha presentado (0 minutos), lo elimine de la cola con remove() y siga 
con continue; si atenderlo haría superar jornada minutos en total, 
termine con break (ese paciente y los demás quedan en la cola); y en 
otro caso lo elimine de la cola, sume sus minutos y lo anote. Devuelve 
una lista de tuplas (nombre, minuto_en_que_termina) en el orden de atención.


En el programa principal: reclasifica a "Nora", "Pablo" y un nombre que 
no exista; atiende con jornada = 60 + 5 * [Z] (sustituye [Z] por el 
último dígito de tu DNI/NIF); y muestra el número de reclasificados, 
la lista de atendidos y los nombres de los pacientes que quedan sin atender.
"""
Z = 8


def siguiente(cola):
    #Posición del paciente a atender: menor prioridad y, a igualdad, el primero
    mejor = 0
    for i in range(1, len(cola)):
        if cola[i][1] < cola[mejor][1]:
            mejor = i
    return mejor


def reclasificar(cola, *nombres):
    #Sube a prioridad 1 a los pacientes indicados. Devuelve cuántos reclasifica
    cambiados = 0
    for nombre in nombres:
        for i, paciente in enumerate(cola):
            if paciente[0] == nombre:
                if paciente[1] != 1:
                    cola.insert(i, (nombre, 1, paciente[2]))
                    cola.remove(paciente)
                    cambiados += 1
                break
    return cambiados


def atender(cola, jornada=240):
    """Atiende la cola hasta agotarla o llegar al límite de jornada.
    Devuelve una lista de (nombre, minuto_en_que_termina).
    """
    atendidos = []
    total = 0
    while cola:
        paciente = cola[siguiente(cola)]
        nombre, _, minutos = paciente
        if minutos == 0:
            cola.remove(paciente)
            continue
        if total + minutos > jornada:
            break
        cola.remove(paciente)
        total += minutos
        atendidos.append((nombre, total))
    return atendidos


cola = [("Lucía", 3, 15), ("Mario", 2, 20), ("Irene", 1, 30), ("Pablo", 3, 0),
        ("Sara", 2, 25), ("Hugo", 1, 10), ("Nora", 3, 20)]

# Pruebas y ejemplos
n = reclasificar(cola, "Nora", "Pablo", "NADIE") # NADIE no deberia aparecer
jornada = 60 + 5 * Z
atendidos = atender(cola, jornada)
sin_atender = []
for p in cola:
    if p[0]:
        sin_atender.append(p)
print("Reclasificados:", n)
print(f"Atendidos (jornada={jornada}):", atendidos)
print("Sin atender:", sin_atender)
