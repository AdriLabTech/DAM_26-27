# Actividad 16. Depuracion de un ValueError

edad_texto = input("Introduce tu edad: ")
edad = int(edad_texto)
print(f"Dentro de 5 años tendras {edad + 5} años.")

# Error de tipo ValueError, ya que el programa espera un numero,
# ya sea entero o decimal para poder castearlo a entero y poder operar con el
# No es un TypeError porque el tipo de dato que pasamos a la funcion int() es
# correcto (la funcion int() admite str como argumento, pero el contenido no se
# puede convertir)
