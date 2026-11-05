"""
Actividad 17 — Captura múltiple en un conversor
Escribe un programa que pida al usuario dos números y
un operador (+, -, *, /) y calcule el resultado. Usa un único
except (ValueError, ZeroDivisionError) as error: para capturar a
la vez el caso de un número no válido y el de una división entre 0,
mostrando el mensaje del error con
print(error)
"""


def operador_valido(operador):
    if len(operador) != 1 or operador not in ("+", "-", "*", "/"):
        raise ValueError("El operador no es correcto")
    return len(operador) == 1 and operador in ("+", "-", "*", "/")


def realizar_operacion(n1, n2, signo):
    match signo:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            return n1 / n2


try:
    primer_numero = int(input("Introduce el primer numero: "))
    segundo_numero = int(input("Introduce el segundo numero: "))
    operador = input("Introduce el operador (+ - * /): ")
    if operador_valido(operador):
        print(realizar_operacion(primer_numero, segundo_numero, operador))
except (ValueError, ZeroDivisionError) as error:
    print(f"[ERROR]: {error}")
