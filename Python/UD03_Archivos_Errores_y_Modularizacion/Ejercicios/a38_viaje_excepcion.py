"""
Actividad 38 — Predice y comprueba: el viaje de una excepción. (Obligatoria)
Seis programas cortos. Antes de ejecutarlos apunte en la bitacora lo que esperaba que
saliera; aqui estan los programas tal cual y, en 3 y 4, tambien la version corregida.
"""

def cabecera(texto):
    print(f"\n===== {texto} =====")

# ---------- Programa 1: finally con return, continue y break ----------
def programa_1():
    def mitad(texto):
        try:
            n = int(texto)
            return n // 2
        except ValueError:
            return -1
        finally:
            # finally se ejecuta SIEMPRE, incluso despues de un return
            print(f"finally({texto})")

    for texto in ["8", "", "x", "-4", "6"]:
        try:
            if texto == "":
                continue   # el finally de abajo tambien se ejecuta con continue
            r = mitad(texto)
            if r < 0:
                break      # ...y tambien con break (el else NO se ejecuta)
        except ValueError:
            print("except")
        else:
            print(f"else {r}")
        finally:
            print("fin de vuelta")
    print("después del bucle")

# ---------- Programa 2: el error sube hasta quien lo captura ----------
def programa_2():
    def leer(precios, producto):
        return precios[producto]

    def informe(precios, producto):
        try:
            precio = leer(precios, producto)
            if precio < 0:
                raise ValueError("precio negativo")
        except ValueError as error:
            print(f"{producto}: {error}")
        else:
            print(f"{producto}: {precio} €")

    precios = {"pan": 1.2, "sal": -1}
    try:
        informe(precios, "pan")
        informe(precios, "sal")
        informe(precios, "té")      # KeyError: informe solo captura ValueError, asi que sube
        informe(precios, "pan")     # no llega a ejecutarse
    except KeyError as error:
        print(f"Capturado fuera: {type(error).__name__} {error}")

# ---------- Programa 3 (original): "except A or B" solo captura A ----------
def programa_3_original():
    datos = [10, 0, "3"]
    for i in range(4):
        try:
            print(100 / datos[i])
        except ZeroDivisionError or TypeError:   # defecto: "A or B" vale solo A
            print("división imposible")
        except Exception as error:
            print(f"inesperado: {type(error).__name__}")

# ---------- Programa 3 (corregido): los dos errores van en una tupla ----------
def programa_3_corregido():
    datos = [10, 0, "3"]
    for i in range(4):
        try:
            print(100 / datos[i])
        except (ZeroDivisionError, TypeError):
            print("división imposible")
        except Exception as error:
            print(f"inesperado: {type(error).__name__}")

# ---------- Programa 4 (original): close() de un archivo que nunca se abrio ----------
def programa_4_original():
    def contar_lineas(ruta):
        try:
            archivo = open(ruta, "r", encoding="utf-8")   # falla aqui: "archivo" no llega a existir
            return len(archivo.readlines())
        finally:
            archivo.close()                                # y aqui se intenta cerrar algo que no existe
    try:
        print(contar_lineas("no_existe.txt"))
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as error:
        print(f"Otro error: {type(error).__name__}")

# ---------- Programa 4 (corregido): with cierra el archivo solo y no hay finally ----------
def programa_4_corregido():
    def contar_lineas(ruta):
        with open(ruta, "r", encoding="utf-8") as archivo:
            return len(archivo.readlines())
    try:
        print(contar_lineas("no_existe.txt"))
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as error:
        print(f"Otro error: {type(error).__name__}")

# ---------- Programa 5: raise a secas y un error dentro de un except ----------
def programa_5():
    def a_numero(texto):
        try:
            return int(texto)
        except ValueError:
            print(f" aviso: {texto!r} no es entero")
            raise   # vuelve a lanzar el mismo error

    for texto in ["4", "2.5", "dos"]:
        try:
            try:
                n = a_numero(texto)
            except ValueError:
                n = int(float(texto))   # si esto falla, el error NO lo recoge el except de al lado
                print(f"{texto}: truncado a {n}")
            else:
                print(f"{texto}: entero {n}")
        except ValueError as error:
            print(f"{texto}: {type(error).__name__}")

# ---------- Programa 6: excepciones habituales y la variable "error" ----------
def programa_6():
    notas = {"Ana": [7, 9], "Luis": []}
    for nombre in ["Ana", "Luis", "Eva"]:
        try:
            lista = notas[nombre]
            print(nombre, lista[1], sum(lista) / len(lista))
        except (KeyError, IndexError) as error:
            print(f"{nombre}: {type(error).__name__} {error}")
    try:
        print("Total: " + 16)
    except TypeError as error:
        mensaje = str(error)
    print(mensaje)
    # Python borra "error" al salir del except: usarla despues da NameError
    try:
        print(error)
    except NameError as fallo:
        print(f"NameError: {fallo}")

for titulo, programa in [
    ("Programa 1", programa_1), ("Programa 2", programa_2),
    ("Programa 3 (original)", programa_3_original), ("Programa 3 (corregido)", programa_3_corregido),
    ("Programa 4 (original)", programa_4_original), ("Programa 4 (corregido)", programa_4_corregido),
    ("Programa 5", programa_5), ("Programa 6", programa_6)]:
    cabecera(titulo)
    programa()
