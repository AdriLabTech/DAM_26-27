"""
Actividad 17 - Calculadora con operador
Calcula dos numeros con el operando que elija el usuario (+ - * /)
"""

def calcular(n1, n2, signo):
    # La cadena de if/elif comprueba el signo uno a uno. Cada rama devuelve el
    # resultado de la operacion correspondiente y el return corta la funcion,
    # asi que en cuanto una coincide ya no se ejecuta el resto
    if signo == "+":
        return n1 + n2
    elif signo == "-":
        return n1 - n2
    elif signo == "*":
        return n1 * n2
    elif signo == "/":
        return n1 / n2
    else:
        # Si el usuario escribe cualquier otra cosa, avisamos en vez de romper
        return "Operacion no permitida..."


# Capturamos las entradas del usuario
numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
signo_operacion = input("Introduce la operacion (+ - * /): ")

# Llamamos a la funcion pasando los tres datos y guardamos lo que devuelve
solucion_operacion = calcular(numero1, numero2, signo_operacion)

print(f"Solucion de la operacion: {solucion_operacion}")