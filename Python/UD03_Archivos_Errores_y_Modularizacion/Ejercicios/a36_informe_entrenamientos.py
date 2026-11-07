"""
Actividad 36 — Informe de entrenamientos desde un CSV. (Obligatoria)
Lee entrenos.csv, descarta las lineas con problemas (apuntandolas en descartes.txt)
y muestra el tiempo y los kilometros de cada deportista frente a un objetivo de 10 km.
"""
lineas = [
    "fecha,deportista,tiempo,km",
    "2026-10-01,Ana,25:30,5",
    "2026-10-01,Luis,31:05,6",
    "2026-10-02,Ana,24:x,5",
    "2026-10-02,Eva,40:10",
    "2026-10-03,Luis,29:45,6,extra",
    "2026-10-03,Ana,26:02,5.5",
    "2026-10-04,Eva,38:00,7",
    "2026-10-04,Luis,30:10,",
]
ruta_csv = "../output/entrenos.csv"
ruta_descartes = "../output/descartes.txt"
OBJETIVO_KM = 10

# Creamos el fichero CSV con la lista de arriba, una linea por elemento
with open(ruta_csv, "w", encoding="utf-8") as f:
    for linea in lineas:
        f.write(linea + "\n")

# Convierte "25:30" en segundos (25*60 + 30). No captura errores: si el texto esta
# mal, el error sube a quien la llama.
def a_segundos(tiempo):
    minutos, segundos = tiempo.split(":")
    return int(minutos) * 60 + int(segundos)

# Hace lo contrario: de segundos a "m:ss" (los segundos siempre con 2 cifras)
def formatear(segundos):
    return f"{segundos // 60}:{segundos % 60:02d}"

# Totales por deportista: uno para el tiempo y otro para los kilometros
tiempos = {}
kilometros = {}

# Un unico "with" abre los dos ficheros: el CSV para leer y descartes.txt para escribir
with open(ruta_csv, "r", encoding="utf-8") as entrada, open(ruta_descartes, "w", encoding="utf-8") as descartes:
    entrada.readline()  # Saltamos la cabecera (la primera linea)
    # start=2 porque la linea 1 era la cabecera: asi el numero coincide con el del fichero
    for numero, linea in enumerate(entrada, start=2):
        linea = linea.strip()

        # Primer try: solo comprueba que la linea tenga justo 4 campos
        try:
            fecha, deportista, tiempo, km = linea.split(",")
        except ValueError:
            descartes.write(f"Línea {numero}: formato incorrecto {linea!r}\n")
            continue  # Pasamos a la siguiente linea

        # Segundo try: comprueba que el tiempo y los km sean valores validos
        try:
            segundos = a_segundos(tiempo)
            km = float(km)
        except ValueError:
            descartes.write(f"Línea {numero}: valor no válido {linea!r}\n")
            continue

        # .get(clave, 0) devuelve 0 si el deportista todavia no esta en el diccionario
        tiempos[deportista] = tiempos.get(deportista, 0) + segundos
        kilometros[deportista] = kilometros.get(deportista, 0) + km

# Mostramos el resumen. {diferencia:+.1f} pone siempre el signo (+ o -) y 1 decimal
for deportista in tiempos:
    diferencia = kilometros[deportista] - OBJETIVO_KM
    print(f"{deportista}: {formatear(tiempos[deportista])} en {kilometros[deportista]} km "
          f"({diferencia:+.1f} km respecto al objetivo)")

# Volvemos a abrir descartes.txt para contar cuantas lineas se descartaron
with open(ruta_descartes, "r", encoding="utf-8") as f:
    descartadas = f.readlines()
print(f"Lineas descartadas: {len(descartadas)}")
for linea in descartadas:
    print("  " + linea.strip())
