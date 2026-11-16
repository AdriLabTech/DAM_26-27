"""
Actividad 19 — Media de temperaturas.
Crea un archivo temperaturas.txt con una temperatura por 
línea. Escribe un programa que calcule la media de todas ellas,
usando try/except para descartar (sin detener el programa) las líneas que no contengan
un número válido
"""
fichero = "../output/a19_temperaturas.txt"

# Cada ejecucion crea el fichero de cero con unos datos de prueba
def preparar_fichero(temperaturas):
    with open(fichero, "w", encoding="utf-8") as f:
        for temperatura in temperaturas:
            f.write(str(temperatura) + "\n")

def calcular_media(fichero):
    suma = 0
    lineas_validas = 0
    with open(fichero, "r", encoding="utf-8") as f:
        for linea in f:
            try:
                suma += float(linea)
                lineas_validas += 1
            except ValueError:
                print(f"Linea descartada: {linea.strip()!r}")
    # Si no hubo ninguna valida devolvemos 0 para no dividir entre 0
    return suma / lineas_validas if lineas_validas != 0 else 0

# "no valido" esta puesto a proposito para probar el descarte
preparar_fichero([12.8, 9.4, 1, 123.5, "no valido"])
print(f"La media de las temperaturas es: {calcular_media(fichero):.2f}")
