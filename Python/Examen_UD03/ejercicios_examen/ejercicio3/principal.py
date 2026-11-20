# Adrian X=8 Y=3
"""
Opción 3 — Lista de tareas con un paquete (3 puntos)

Qué hace el programa. Guarda tareas en el fichero tareas.txt, una por línea, y cuenta cuántas hay. Las funciones van en un paquete.
3. En principal.py:

    a) Importa las funciones: from utilidades.textos import anadir, contar.
    b) Pega los datos de la opción 3. Borran el fichero de pruebas anteriores y crean la lista tareas.
    c) Muestra Antes: y el resultado de contar(RUTA).
    d) Recorre la lista tareas y llama a anadir(RUTA, tarea) con cada una.
    e) Muestra Después: y el resultado de contar(RUTA).

Salida esperada (igual para todos):

Antes: 0
Después: 3

Contenido de tareas.txt con [X] = 7 e [Y] = 3 (con tus dígitos cambian los dos números):

Repasar el tema 7
Hacer 3 ejercicios
Entregar la práctica
"""
# 1.- Importa las funciones: from utilidades.textos import anadir, contar.

# Importo el fichero textos del paquete utilidades, asigandole un alias 't'
from utilidades import textos as t

# Importo la libreria os para trabajar con ficheros y directorios del sistema
import os

# Ruta del fichero de tareas
fichero_tareas = "ficheros/tareas.txt"

# Limpio el fichero para que la salida salga igual
if os.path.exists(fichero_tareas):
    with open(fichero_tareas, "w", encoding="utf-8"):
        print("Archivo limpio (para que la salida salga igual)")

# 3.- Muestra Antes: y el resultado de contar(RUTA)
print(f"Antes: {t.contar(fichero_tareas)}")

# 4.- Recorre la lista tareas y llama a anadir(RUTA, tarea) con cada una.

# Agrego las tareas una por una antes de mostrar el resultado final
t.anadir(fichero_tareas, "Repasar el tema 8")
t.anadir(fichero_tareas, "Hacer 3 ejercicios")
t.anadir(fichero_tareas, "Entregar la práctica")

# 5.- Muestra Después: y el resultado de contar(RUTA).
print(f"Despues: {t.contar(fichero_tareas)}")

