"""
Actividad 5 — División seguida de errores
Pide dos números al usuario y muestra el resultado de dividir 
el primero entre el segundo. Captura con try/except tanto el caso de 
que el usuario no introduzca un número válido (ValueError) como el caso de
dividir entre 0 (ZeroDivisionError), mostrando un mensaje distinto para cada error
"""
# Intentamos hacer la division; si algo sale mal, saltamos a un "except"
try:
    numero1 = int(input("Introduce el primer numero: "))
    numero2 = int(input("Introduce el segundo numero: "))
    print(f"Resultado de la division: {numero1 / numero2}")
# Si lo escrito no es un numero entero, avisamos
except ValueError:
    print("No se puede dividir por algo que no es un número...")
# Si el segundo numero es 0, avisamos con otro mensaje distinto
except ZeroDivisionError:
    print("No se puede dividir por cero...")
