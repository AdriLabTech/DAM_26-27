# Actividad 11. Comprobacion de mayoria de edad y descuento

edad_usuario = int(input("Introduzca su edad: "))

# Comprobamos que la edad del usuario sea valida (mayor que 0)
while(edad_usuario < 0):
    edad_usuario = int(input("Introduzca una edad valida: "))


# Pedimos al usuario que introduzca si o no y en caso de que introduzca algo no valido, volvemos a preguntar
entrada_usuario_carnet = input("Tiene carne joven? (si/no): ")
while(entrada_usuario_carnet != "si" and entrada_usuario_carnet != "no"):
    entrada_usuario_carnet = input("Tiene carne joven? (si/no): ")

# Si el usuario introduce si, el valor de la variable tiene_carnet es True
tiene_carnet = entrada_usuario_carnet == "si"

condicion_mayor_y_carne = edad_usuario >= 18 and tiene_carnet

condicion_mayor_o_carne = edad_usuario >= 18 or tiene_carnet

if condicion_mayor_y_carne:
    print("Es mayor de edad Y tiene carne!!!")

elif condicion_mayor_o_carne:
    print("Es mayor de edad O tiene carne!!!")

# Imprimimos el valor de las condiciones (ambas variables son de tipo bool)
print(f"Valor Booleano de la condicion 'Es mayor de edad Y tiene carne': {condicion_mayor_y_carne}")

print(f"Valor Booleano de la condicion 'Es mayor de edad O tiene carne': {condicion_mayor_o_carne}")

