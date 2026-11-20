# Adrian - X=8 Y=3
"""
Opción 1 — Sumar las ventas de un fichero (3 puntos)

Qué hace el programa. Lee el fichero ventas.txt, que tiene un número en cada línea, y suma los números. Una de las líneas está mal escrita a propósito. El fichero contiene:

12[X]
80
abc
4[Y]
30

Archivos. Crea dos: ventas.py y principal.py.

1. En ventas.py, escribe la función sumar(ruta):

    a) Abre el fichero con with y recórrelo línea a línea.
    b) Convierte cada línea con int(linea) y súmala a un total.
    c) Si la línea no es un número, int lanza ValueError. Captúralo y suma 1 a un contador de errores. El programa sigue con la línea siguiente.
    d) Al final, devuelve las dos cosas: return total, errores. La función no imprime nada.
"""

# Importo la libreria os para trabajar con ficheros y directorios del sistema
import os


# Metodo para sumar todos los valores numericos de las lineas del fichero
def sumar(ruta):
    errores = 0
    total = 0

    # Verifico que el fichero existe
    if os.path.exists(ruta):
        # Abro el fichero en modo lectura para poder leer su contenido
        with open(ruta, "r", encoding="utf-8") as fichero:
            # Itero por cada linea e intento convertir cada una de estas en numero
            for linea in fichero:
                try:
                    total += int(linea)
                    # En caso de que la linea no sea un numero, agrego 1 al contador de errores
                except ValueError:
                    errores += 1
                    continue
    else:
        # En caso de que el fichero no exista, mando el mensaje correspondiente
        raise FileNotFoundError(f"No existe el fichero {os.path.basename(ruta)}")
    return total, errores

