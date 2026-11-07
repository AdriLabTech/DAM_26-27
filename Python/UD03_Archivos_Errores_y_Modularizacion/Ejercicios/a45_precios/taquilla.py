"""
Actividad 45 — Rediseña un módulo mal hecho. (Voluntaria)
Procesa las ventas, anula las incorrectas y muestra lo recaudado.
Ejecutar desde esta carpeta: python taquilla.py
"""
from precios import precio, PrecioError

ventas = [("normal", "2"), ("infantil", "3"), ("reducida", "dos"), ("reducida", "4")]

recaudado = 0
for tarifa, entradas in ventas:
    try:
        importe = precio(tarifa, entradas)
    except PrecioError as error:
        # Venta incorrecta: se anula y no suma nada
        print(f"{tarifa}, {entradas}: ANULADA ({error})")
    else:
        recaudado += importe
        print(f"{tarifa}, {entradas}: {importe:.2f} €")

print(f"Recaudado: {recaudado:.2f} €")
