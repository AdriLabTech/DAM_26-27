"""
Actividad 18 - Saludo personalizable
Escribe una función saludar(nombre="Estudiante", idioma="es") con dos parámetros con
valor por defecto: si idioma es "es" saluda en español, si es "en" saluda en inglés. Llama a
la función de tres formas distintas: sin argumentos, indicando solo el nombre, e indicando
ambos
"""


# Los dos parametros llevan valor por defecto entre el signe igual, asi que se
# pueden omitir al llamar a la funcion
def saludar(nombre="Estudiante", idioma="es"):
    # Con una condicional ternaria elegimos el saludo segun el idioma
    print(f"Hello {nombre}" if idioma == "en" else f"Hola {nombre}")


# 1) Sin argumentos: se usan los dos valores por defecto
saludar()

# 2) Solo el nombre: el idioma se queda en su valor por defecto
saludar("Adrian")

# 3) Los dos parametros: aqui si se indica el idioma, cambia el saludo
saludar("Adrian", "en")