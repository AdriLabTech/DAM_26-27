"""
Actividad 27 — Registro de errores en archivo. (Obligatoria) Escribe un programa que
pida al usuario varios números y calcule 100 dividido entre cada uno. Cada vez que se
produzca un error (división entre 0, o texto no numérico), en lugar de solo mostrarlo por
pantalla, debe escribirse una línea describiéndolo en un archivo errores.log (modo “a”), de
forma que al final del programa el archivo contenga un histórico de todos los errores
ocurridos durante la ejecución
"""
fichero = "../output/errores.log"

def añadir_informe(error):
    # Modo "a" para conservar los errores de ejecuciones anteriores
    with open(fichero, "a", encoding="utf-8") as f:
        f.write(error + "\n")
    print("Error guardado en errores.log")

# Primero pedimos todos los numeros...
lista_numeros = []
while True:
    entrada_usuario = input("Introduce un numero (o sal con 'fin'): ")
    if entrada_usuario == "fin":
        break
    lista_numeros.append(entrada_usuario)

# ...y despues calculamos 100 entre cada uno
for n in lista_numeros:
    try:
        resultado = 100 / int(n)
        print(f"100 / {n} = {resultado}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"[ERROR]: {e}")
        añadir_informe(f"[ERROR]: {e}")
