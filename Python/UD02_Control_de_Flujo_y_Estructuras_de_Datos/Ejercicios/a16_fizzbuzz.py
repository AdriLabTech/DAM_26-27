"""
Actividad 16. FizzBuzz clásico. (Voluntaria — ampliación)
Recorre los números del 1 al 50 y muestra “Fizz” si el número es múltiplo de 3, “Buzz” si es
múltiplo de 5, “FizzBuzz” si es múltiplo de ambos, o el propio número en caso contrario.
"""

# range(1, 50) recorre del 1 al 49, porque range() nunca llega al ultimo valor
for i in range(1, 50):
    # El caso dificil es el numero divisible por 3 y por 5 a la vez, porque es
    # multiple de los dos. Por eso dentro del "si es multiplo de 3" miramos
    # tambien el 5: si tambien lo es, imprimimos FizzBuzz; si no, solo Fizz
    if i % 3 == 0:
        print(f"{i}: FizzBuzz" if i % 5 == 0 else f"{i}: Fizz")
    elif i % 5 == 0:
        # Los que son multiplos de 3 ya se han comprobado arriba, asi que aqui
        # solo llegan los que son multiplos de 5 pero no de 3
        print(f"{i}: Buzz")
    else:
        print(i)