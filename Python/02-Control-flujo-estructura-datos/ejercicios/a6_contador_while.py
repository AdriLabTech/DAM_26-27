"""
Actividad 6. Contador con while
Escribe un programa que pida números al usuario, uno tras otro, hasta que introduzca un
0. Al terminar, muestra cuántos números se han introducido (sin contar el 0) y su suma
total.
"""
# primero cremos la variable asigandole un valor distinto de 1
# para posteriormente usar un while y preguntar constantemente hasta
# que introduzca el 0

num = 1
contador = 0 # creamos el contador de numeros introducidos

while(num != 0):
    num = int(input("Introduce un numero: "))
    if(num != 0):
        contador += 1
print(f"Cantidad de numeros introducidos: {contador}")
