"""
Actividad 13. Adivina el número
Genera un número aleatorio entre 1 y 100 con random.randint(). Usando un bucle while
con un máximo de 10 intentos, pide al usuario que lo adivine, dando la pista “mayor” o
“menor” tras cada intento.
"""
# Importamos la libreria random
import random
# Generamos el numero aleatorio
rand_num = random.randint(1, 100)
numero_adivinado = False
intentos = 0

while numero_adivinado == False and intentos <= 10:
    numero_a_probar = int(input("Introduce un numero: "))
    if numero_a_probar < rand_num:
        print("El numero a adivinar es mas GRANDE")
        intentos += 1
    elif numero_a_probar > rand_num:
        print("El numero a adivinar es mas PEQUEÑO")
        intentos += 1
    else:
        print("Numero adivinado!!!")
        numero_adivinado = True