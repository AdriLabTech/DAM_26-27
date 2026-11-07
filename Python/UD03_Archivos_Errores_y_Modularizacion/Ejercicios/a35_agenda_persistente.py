"""
Actividad 35 — Reto: agenda de contactos persistente. (Obligatoria) Amplía la actividad
25 para construir una pequeña agenda con menú (while) que permita: añadir un contacto,
listar todos los contactos, buscar un contacto por nombre, y salir. Todo el acceso a
archivos debe ir protegido con try/except, y al menos las funciones de gestión de
contactos deben estar en un módulo separado (contactos.py), no en el archivo principal.
Antes de terminar, comprueba que si cierras el programa y lo vuelves a ejecutar, los
contactos añadidos anteriormente siguen ahí.
"""
from modulos import contactos

# Los contactos se guardan en un fichero, asi que siguen ahi la proxima vez que se ejecute
while True:
    print("\n=== AGENDA ===")
    print("1. Añadir contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Salir")
    opcion = input("Elige una opcion: ")

    # Todas las operaciones con el fichero van dentro de un try/except
    try:
        if opcion == "1":
            contactos.añadir_contacto(input("Nombre: "), input("Telefono: "))
        elif opcion == "2":
            contactos.listar_contactos()
        elif opcion == "3":
            contactos.buscar_contacto(input("Nombre a buscar: "))
        elif opcion == "4":
            print("Hasta pronto")
            break
        else:
            print("Opcion no valida")
    except FileNotFoundError:
        print("[AVISO]: todavia no hay contactos guardados")
    except contactos.ContactoNoEncontradoError as e:
        print(f"[AVISO]: {e}")
    except (ValueError, OSError) as e:
        print(f"[ERROR]: {e}")
