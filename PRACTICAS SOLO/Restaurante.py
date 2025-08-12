#Factura de restaurante
#Un restaurante ofrece 3 platos principales y 2 bebidas con precios fijos. El cliente elige un plato y una bebida, 
#se aplica un IVA del 12 % sobre el subtotal y una propina del 10 % también sobre el subtotal.

#Entradas: precio del plato, precio de la bebida.
#Salida: subtotal, importe de IVA, importe de propina y total a pagar.

# Primero tengo que mostrar los platos y bebidas, luego tengo que pedirle lo que el cliente elija del menu,
# Luego tengo que sumar el precio de el plato y la bebida, 
# luego tengo que calcular el IVA del 12% y la propina del 10%
# Y por ultimo tengo que imprimir el subtotal con el iva y la propina, y al final el total a pagar.
Menu = {
    "Frijoles":50,
    "Lentejas":70,
    "Arroz chino":80,
    "Agua":10,
    "Pony malta":15
}
print("Bienvenido al restaurante \n elige tu menu: :)")
for nombre, precio in Menu.items():
    print(f"{nombre}: {precio}")

Plato = input("Elige un plato: ")
Bebida = input("Elige una bebida: ")

Subtotal = Menu[Plato] + Menu[Bebida]

IVA = Subtotal * 0.12
Propina = Subtotal * 0.10

Total = Subtotal + IVA + Propina

print(f"\n\n\nTu factura es: \n\nSubtotal: {Subtotal} \nIVA: {round(IVA,3)}\nPropina: {Propina} \nY el total a pagar es: {Total}\n\n\n")