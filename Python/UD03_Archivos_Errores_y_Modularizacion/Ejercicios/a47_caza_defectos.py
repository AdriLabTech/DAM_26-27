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
    # Defectos 3 y 1: "with" cierra el archivo solo (sin finally) y el modo "a" añade al final
    with open(ruta, "a", encoding="utf-8") as archivo:
        # Defecto 2: el "\n" deja cada alerta en su linea
        archivo.write(texto + "\n")

open(ruta, "w", encoding="utf-8").close()
for texto in ["Puerta abierta", "", "Humo en cocina"]:
    try:
        guardar(texto)
    # Defecto 4: lo concreto (AlertaError) va antes que lo general (Exception)
    except AlertaError as error:
        print(f"No guardada: {error}")
    except Exception:
        print("Error desconocido")
with open(ruta, "r", encoding="utf-8") as archivo:
    print(f"Alertas guardadas: {len(archivo.readlines())}")
