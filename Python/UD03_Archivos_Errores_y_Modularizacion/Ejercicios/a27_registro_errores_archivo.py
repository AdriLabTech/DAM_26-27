"""
Actividad 27 — Registro de errores en archivo. (Obligatoria) Escribe un programa que
pida al usuario varios números y calcule 100 dividido entre cada uno. Cada vez que se
produzca un error (división entre 0, o texto no numérico), en lugar de solo mostrarlo por
pantalla, debe escribirse una línea describiéndolo en un archivo errores.log (modo “a”), de
forma que al final del programa el archivo contenga un histórico de todos los errores
ocurridos durante la ejecución
"""
fichero = "../output/errores.log"

# Escribe una linea de error al final del log
def añadir_informe(error):
    # Modo "a": anade al final sin borrar los errores de ejecuciones anteriores
    with open(fichero, "a", encoding="utf-8") as f:
        f.write(error + "\n")
    print("Error guardado en errores.log")

# Primero recogemos todos los numeros que escriba el usuario
lista_numeros = []
while True:
    entrada_usuario = input("Introduce un numero (o sal con 'fin'): ")
    if entrada_usuario == "fin":
        break
    lista_numeros.append(entrada_usuario)

# Despues calculamos 100 entre cada uno (antes estaba al reves: n / 100)
for n in lista_numeros:
    try:
        resultado = 100 / int(n)
        print(f"100 / {n} = {resultado}")
    except (ValueError, ZeroDivisionError) as e:
        # Ademas de mostrar el error, lo apuntamos en el fichero
        print(f"[ERROR]: {e}")
        añadir_informe(f"[ERROR]: {e}")
