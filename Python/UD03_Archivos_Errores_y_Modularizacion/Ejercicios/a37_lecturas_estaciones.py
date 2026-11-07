"""
Actividad 37 — Lecturas por estaciones con secciones. (Obligatoria)
Lee lecturas.ini (secciones [Estacion] con lineas hora = valor) y devuelve los datos
y la lista de errores encontrados.
"""
contenido = """# Lecturas de temperatura
08:00 = 14.5
[Norte]
08:00 = 12.5
08:10 =
08:20 = 13.0 ; revisado

[Sur]
08:00 = --
08:10 = 18.25
09:00 = 19
sin igual
"""
ruta = "../output/lecturas.ini"
with open(ruta, "w", encoding="utf-8") as archivo:
    archivo.write(contenido)

# Devuelve (datos, errores). No imprime nada: de eso se encarga el programa principal.
def leer_lecturas(ruta):
    datos = {}       # {estacion: {hora: valor}}
    errores = []     # mensajes de las lineas con problemas
    actual = None    # estacion en la que estamos ahora (None = todavia ninguna)
    ultimo = None    # ultimo valor valido de la estacion actual

    with open(ruta, "r", encoding="utf-8") as f:
        for numero, linea in enumerate(f, start=1):
            # Quitamos el comentario del final (lo que va tras ";") y los espacios
            linea = linea.split(";")[0].strip()
            # Ignoramos lineas vacias y las que empiezan por #
            if linea == "" or linea.startswith("#"):
                continue

            # Linea [Nombre]: empieza una seccion nueva
            if linea.startswith("[") and linea.endswith("]"):
                actual = linea[1:-1]
                datos[actual] = {}
                ultimo = None  # Cada seccion empieza sin valor anterior
                continue

            # Una linea de datos tiene que llevar "="
            if "=" not in linea:
                errores.append(f"Línea {numero}: falta '=' en {linea!r}")
                continue

            # Un dato antes de cualquier seccion no sabemos a que estacion pertenece
            if actual is None:
                errores.append(f"Línea {numero}: dato fuera de sección")
                continue

            hora, texto = linea.split("=", 1)
            hora, texto = hora.strip(), texto.strip()
            try:
                valor = float(texto)
            except ValueError:
                # Valor vacio o "--": usamos el ultimo valor bueno de esta seccion
                if ultimo is None:
                    errores.append(f"Línea {numero}: {texto!r} sin valor anterior")
                    continue
                valor = ultimo
            datos[actual][hora] = valor
            ultimo = valor
    return datos, errores

datos, errores = leer_lecturas(ruta)
print("Datos:")
print(datos)
print("Errores:")
for error in errores:
    print("  " + error)
print(f"Norte a las 08:10 -> {datos['Norte']['08:10']}")
