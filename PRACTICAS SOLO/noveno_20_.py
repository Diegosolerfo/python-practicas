#Crear un programa que se ejecute N veces, donbde N es el numero de clientes, por cada cliente 
#se va a calcular el 15% de descuento en su compra y se va a imprmir el total a apagar

#Paso a paso:
# 1. Pedir el numero de clientes y ejecutar el ciclo para que pida los datos al usuario o cajero
clientes = int(input("Ingrese el numero de clientes: "))
mayores = input("Habilitar que el descuento se aplique a compras de mas de 100000: (si/no): ").lower()
if mayores == "si":
    mayores = True
    if clientes >= 0:
        for i in range(clientes):
            # 2. Pedir el valor de la compra
            compra = float(input("Ingrese el valor de la compra: "))
            # 3. Calcular el 15% de descuento
            # 3.1 Si es mayor a 100000 se calcula el 15% de descuento
            if compra > 100000:
                descuento = compra * 0.15
                total = compra - descuento
            else:
                total = compra
            # 4. Imprimir el total a pagar
                print(f"El total a pagar es: {total}")
    else:
        print("El numero de clientes no puede ser negativo")
else:
    mayores = False
    if clientes >= 0:
        for i in range(clientes):
            # 2. Pedir el valor de la compra
            compra = float(input("Ingrese el valor de la compra: "))
            # 3. Calcular el 15% de descuento
            # 3.1 Si es mayor a 100000 se calcula el 15% de descuento
            descuento = compra * 0.15
            total = compra - descuento
            total = compra
            # 4. Imprimir el total a pagar
            print(f"El total a pagar es: {total}")
    else:
        print("El numero de clientes no puede ser negativo")
# 5. Fin del programa