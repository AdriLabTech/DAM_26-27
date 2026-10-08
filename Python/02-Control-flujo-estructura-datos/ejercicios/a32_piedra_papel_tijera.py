"""
Actividad 32 - Piedra, papel o tijera
Escribe una función jugar(eleccion_usuario, eleccion_pc) que determine quién gana la
partida. Usa random.choice() para la elección del ordenador y repite varias rondas con un
bucle, llevando la cuenta de victorias de cada jugador
"""
# Para poder comparar las jugadas con operadores las tratamos como numeros:
# piedra = 0 | papel = 1 | tijera = 2
#
# La clave esta en restar las dos jugadas y mirar el resto al dividir entre 3,
# porque la diferencia siempre cae en 0, 1 o -1 (o 2, o -2):
#   - Si la diferencia es 0, las jugadas son la misma: empate
#   - Si al restar sale 1, gana el usuario (piedra(0) vs tijera(2), papel(1) vs piedra(0)...)
#   - Si al restar sale -1, gana la maquina (tijera(2) vs piedra(0), ...)
import random as rnd

def jugar(eleccion_usuario, eleccion_pc):
    diferencia = eleccion_usuario - eleccion_pc

    if diferencia % 3 == 0:
        print("Empate")
    elif diferencia % 3 == 1:
        print("Gana el usuario")
    else:
        print("Gana la maquina")

# Repetimos 5 rondas. En cada una el ordenador elige al azar entre las tres
# opciones y el usuario introduce la suya por teclado
for i in range(0, 5):
    eleccion_pc = rnd.choice([0, 1, 2])
    eleccion_usuario = int(input("Introduce tu jugada (piedra - 0/ papel - 1/ tijeras - 2): "))
    jugar(eleccion_usuario, eleccion_pc)
