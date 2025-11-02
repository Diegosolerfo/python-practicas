print("Digite la cantidad de ventas realizadas: ")
numVentas = int(input())
while numVentas > 0:
    print("Digite el monto de la venta y el descuento: ")
    montoVenta = float(input("Monto venta: "))
    descuento = float(input("Descuento: "))
    total = (montoVenta * descuento) / 100
    print(f"\nEl total a pagar es: ", montoVenta - total, "\n")
    numVentas -= 1