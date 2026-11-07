"""
Actividad 19 — Media de temperaturas.
Crea un archivo temperaturas.txt con una temperatura por 
línea. Escribe un programa que calcule la media de todas ellas,
usando try/except para descartar (sin detener el programa) las líneas que no contengan
un número válido
"""
fichero = "../output/a19_temperaturas.txt"

# Creamos el fichero de cero en cada ejecucion con unos datos de prueba.
# Antes se anadian datos nuevos cada vez y el fichero crecia sin control.
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
                # Si la linea no es un numero, float() falla y pasamos a la siguiente
                suma += float(linea)
                lineas_validas += 1
            except ValueError:
                print(f"Linea descartada: {linea.strip()!r}")
    # Evitamos dividir entre 0 si no habia ninguna temperatura valida
    return suma / lineas_validas if lineas_validas != 0 else 0

# Una de las lineas ("no valido") es erronea a proposito
preparar_fichero([12.8, 9.4, 1, 123.5, "no valido"])
print(f"La media de las temperaturas es: {calcular_media(fichero):.2f}")
