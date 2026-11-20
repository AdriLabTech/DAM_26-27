"""
Opción 3 — Lista de tareas con un paquete (3 puntos)

Qué hace el programa. Guarda tareas en el fichero tareas.txt, una por línea, y cuenta cuántas hay. Las funciones van en un paquete.

Archivos. Crea esta estructura dentro de tu carpeta:

utilidades/
    __init__.py      (archivo vacío: hace que la carpeta sea un paquete)
    textos.py        (pasos 1 y 2)
principal.py         (paso 3)

1. En utilidades/textos.py, escribe la función anadir(ruta, texto). Abre el fichero en 
modo "a" y escribe el texto con un salto de línea al final.

2. En el mismo archivo, escribe la función contar(ruta):

    a) Abre el fichero para leer y devuelve cuántas líneas tiene.
    b) Si el fichero no existe, Python lanza FileNotFoundError. Captúralo dentro de la función y devuelve 0.
"""
# Importo la libreria os para trabajar con ficheros y directorios del sistema
import os

# Metodo para añadir una nueva tarea dentro de un fichero
def anadir(ruta, texto):
    # Verifico que el archivo existe
    if os.path.exists(ruta):
        # Lo abro con el permiso 'a', que permite agregar contenido sin sobreescribirlo
        with open(ruta, "a", encoding="utf-8") as fichero:
            # Escribo la nueva tarea dentro del fichero
            fichero.write(f"{texto}\n")

# Metodo para contar cuantas lineas tiene un fichero
def contar(ruta):
    # Intento abrir el archivo, preparando la excepcion por si no existe
    try:
        with open(ruta, "r", encoding="utf-8") as fichero:
            # Cuento la longitud de n (lineas) usando una compresion
            # VERSION CON BUCLE TRADICIONAL
            """
            contador = 0
            for n in fichero:
                contador += 1
            return contador
            """
            return len([n for n in fichero])
        # En caso de que el fichero no exista, lanzo una excepcion avisando de ello
    except FileNotFoundError("[ERROR]: Archivo no encontado"):
        return 0