"""
Actividad 13. Adivina el número
Genera un número aleatorio entre 1 y 100 con random.randint(). Usando un bucle while
con un máximo de 10 intentos, pide al usuario que lo adivine, dando la pista “mayor” o
“menor” tras cada intento.
"""
# Importamos la libreria random para poder generar numeros al azar
import random

# randint(1, 100) incluye los dos extremos, asi que da un numero entre 1 y 100
rand_num = random.randint(1, 100)

# Estas dos variables son las que controlan el bucle: una indica si ya hemos
# acertado y la otra cuenta los intentos que llevamos
numero_adivinado = False
intentos = 0

# El while se repite mientras NO se haya acertado Y queden intentos (los dos
# controles a la vez, unidos con and)
while numero_adivinado == False and intentos <= 10:
    numero_a_probar = int(input("Introduce un numero: "))

    if numero_a_probar < rand_num:
        print("El numero a adivinar es mas GRANDE")
        intentos += 1
    elif numero_a_probar > rand_num:
        print("El numero a adivinar es mas PEQUEÑO")
        intentos += 1
    else:
        # Cuando acierta no se incrementa intentos y se cambia la bandera, con
        # lo que el while deja de cumplirse en la siguiente vuelta
        print("Numero adivinado!!!")
        numero_adivinado = True