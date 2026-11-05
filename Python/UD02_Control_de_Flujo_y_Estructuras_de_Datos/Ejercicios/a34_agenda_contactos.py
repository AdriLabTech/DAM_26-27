"""
Actividad 34 - Agenda de contactos
Crea una lista vacía de contactos, donde cada contacto es un diccionario con las claves
"nombre" y "telefono". En un bucle, permite al usuario añadir contactos (mientras no
escriba "fin" como nombre). Al finalizar, recorre la lista con for y muestra todos los
contactos con el formato Nombre: <nombre> - Teléfono: <telefono>
"""
# Cada elemento de la lista sera un diccionario con los datos de un contacto
contactos = []

entrada_usuario = ""
# La bandera "terminar" controla el bucle. Se inicializa comparando la entrada
# vacia con "fin", que da False, para que el while entre
terminar = entrada_usuario == "fin"

while terminar == False:
    nombre_contacto = input("Introduce el nombre del contacto (o 'fin' para salir): ")

    if nombre_contacto == "fin":
        terminar = True
        break

    telefono_contacto = input("Introduce el telefono del contacto: ")

    # Creamos el diccionario del contacto y lo anadimos a la lista
    contacto = {
        "nombre": nombre_contacto,
        "telefono": telefono_contacto
    }
    contactos.append(contacto)

# Recorremos la lista de contactos y mostramos cada uno con el formato pedido
for cont in contactos:
    print("FICHA DEL CONTACTO")
    print(f"Nombre: {cont['nombre']} - Telefono: {cont['telefono']}")