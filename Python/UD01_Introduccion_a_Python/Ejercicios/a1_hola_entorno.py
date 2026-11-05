"""
# ----------------------------------------
# Actividad 1. Configuracion del entorno
# ----------------------------------------
Vamos a comprobar si el entorno de Python esta
correctamente configurado. Para eso, importamos
la libreria sys para ejecutar comandos del sistema.

Ejecutamos sys.version para mostrar la version de Python
y el ejeuctable muestra si estamos usando el entorno virtual
"""

import sys
print("¡Entorno configurado correctamente!")
print("Versión de Python:", sys.version)
print("Ejecutable en uso:", sys.executable)
