"""
Actividad 47 — Caza de defectos. (Voluntaria)
Version ORIGINAL (con los 4 defectos) en el comentario; debajo, la version corregida.

    def guardar(texto):
        if texto == "":
            raise AlertaError("alerta vacía")
        try:
            archivo = open("alertas.txt", "w", encoding="utf-8")   # defecto 1: "w" borra lo anterior
            archivo.write(texto)                                   # defecto 2: no escribe el salto de linea
        finally:
            archivo.close()                                        # defecto 3: si open() falla, "archivo" no existe
    ...
    except Exception:                                              # defecto 4: captura TODO y deja
        print("Error desconocido")                                 #   a AlertaError sin llegar nunca
    except AlertaError as error:
        print(f"No guardada: {error}")
"""
ruta = "../output/alertas.txt"

class AlertaError(Exception):
    pass

def guardar(texto):
    if texto == "":
        raise AlertaError("alerta vacía")
    # Defecto 3 corregido: "with" cierra el archivo solo y no hace falta finally.
    # Defecto 1 corregido: modo "a" (anadir al final) en vez de "w" (borrar y escribir).
    with open(ruta, "a", encoding="utf-8") as archivo:
        # Defecto 2 corregido: el "\n" deja cada alerta en su propia linea.
        archivo.write(texto + "\n")

# Vaciamos el fichero antes de empezar
open(ruta, "w", encoding="utf-8").close()
for texto in ["Puerta abierta", "", "Humo en cocina"]:
    try:
        guardar(texto)
    # Defecto 4 corregido: lo mas concreto (AlertaError) va PRIMERO y lo general (Exception) despues.
    except AlertaError as error:
        print(f"No guardada: {error}")
    except Exception:
        print("Error desconocido")
with open(ruta, "r", encoding="utf-8") as archivo:
    print(f"Alertas guardadas: {len(archivo.readlines())}")
