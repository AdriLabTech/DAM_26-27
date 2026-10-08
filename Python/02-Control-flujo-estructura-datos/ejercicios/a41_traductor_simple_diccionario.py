"""
Actividad 41 - Traductor simple con diccionario
Crea un diccionario español-inglés con al menos 10 palabras. Escribe un programa que
traduzca las palabras que el usuario introduzca, usando .get() para avisar cuando una
palabra no está en el diccionario
"""
# Diccionario de traducciones: la clave es la palabra en español y el valor su
# equivalente en ingles
palabras = {
    "hola": "hello",
    "perro": "dog",
    "adios": "bye",
    "gato": "cat",
    "portatil": "laptop",
    "agua": "water",
    "telefono": "phone",
    "auriculares": "headphones",
    "raton": "mouse",
    "alfombrilla": "mousepad"
}

palabra = input("Ingresa una palabra para ver si podemos traducirla: ")

# .get() con un valor por defecto: si la palabra esta en el diccionario devuelve
# la traduccion y si no encuentra el texto "No encontrada", sin lanzar un KeyError
print(f"Traduccion: {palabras.get(palabra, 'No encontrada')}")