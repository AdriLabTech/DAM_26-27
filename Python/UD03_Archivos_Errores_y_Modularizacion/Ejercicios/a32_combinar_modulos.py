"""
Actividad 32 — Combinar dos módulos propios. (Voluntaria) Escribe un programa main.py que
importe dos de los módulos creados en esta unidad (por ejemplo, validaciones.py y
contactos.py) y muestre un menú que use funciones de ambos módulos.
"""
# Importamos dos modulos propios a la vez
from modulos import validaciones, contactos

while True:
    print("\n1. Validar una nota   (modulo validaciones)")
    print("2. Añadir contacto    (modulo contactos)")
    print("3. Listar contactos   (modulo contactos)")
    print("4. Buscar contacto    (modulo contactos)")
    print("5. Salir")
    opcion = input("Elige una opcion: ")

    try:
        if opcion == "1":
            nota = float(input("Nota: "))
            validaciones.validar_nota(nota)
            print("Nota correcta")
        elif opcion == "2":
            contactos.añadir_contacto(input("Nombre: "), input("Telefono: "))
        elif opcion == "3":
            contactos.listar_contactos()
        elif opcion == "4":
            contactos.buscar_contacto(input("Nombre a buscar: "))
        elif opcion == "5":
            print("Adios")
            break
        else:
            print("Opcion no valida")
    # Un solo bloque recoge los errores de los dos modulos
    except (ValueError, FileNotFoundError, contactos.ContactoNoEncontradoError) as e:
        print(f"[ERROR]: {e}")
