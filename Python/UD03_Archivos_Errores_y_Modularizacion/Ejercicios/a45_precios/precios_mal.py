# archivo: precios_mal.py
TARIFAS = {"normal": 8.5, "reducida": 6.0}

def precio(tarifa, entradas):
    if tarifa not in TARIFAS:
        print("Tarifa no encontrada")
        return -1
    return TARIFAS[tarifa] * int(entradas)

print("precios_mal cargado")
print(precio("normal", 2))
