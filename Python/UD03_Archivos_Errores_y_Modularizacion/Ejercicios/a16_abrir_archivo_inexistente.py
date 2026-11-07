"""
Actividad 16 — Abrir un archivo que podría no existir. (Obligatoria) Escribe un programa
que intente leer un archivo inventario.txt. Si el archivo no existe, debe capturar el error
FileNotFoundError, avisar al usuario y crear el archivo vacío para la próxima vez.
"""
path_fichero = "../output/a16_fichero_inexistente.txt"

def leer_fichero(fichero):
    # Intentamos abrir el fichero directamente
    try:
        with open(fichero, "r", encoding="utf-8") as f:
            print(f"Contenido: '{f.read()}'")
    # Si no existe, Python lanza FileNotFoundError y lo capturamos aqui
    except FileNotFoundError:
        print("[AVISO]: El fichero no existe. Se crea vacio para la proxima vez")
        # Abrir en modo "w" y cerrar deja un fichero vacio
        with open(fichero, "w", encoding="utf-8"):
            pass

# La primera vez avisa y crea el fichero; la segunda ya lo encuentra
leer_fichero(path_fichero)
leer_fichero(path_fichero)
