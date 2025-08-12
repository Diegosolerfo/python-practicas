#Servicio de taxi
#Una compañía de taxis cobra: bajada de bandera 2 €, 1 € por kilómetro recorrido y 0,50 € por minuto de espera. Además, 
#aplica un recargo fijo del 20 % sobre el subtotal por servicio nocturno.
#Entradas: kilómetros recorridos, minutos de espera.
#Salida: subtotal, recargo nocturno y coste total.

#Primero definir los datos, subtotal, si hay recargo nocturno, total, tiempo espera, y killometros recorrdios
#Despues se define el proceso, que es preguntar al usuario primero
#Luego hacer el prodcedimiento matematico para dar la salida
#Imprimir el resultado final o la factura del viaje por taxi

#Definicion de datos
Kil = int(input("¿Cuantos kilometros recorrio?: "))
Tie_Esp = int(input("¿Cuantos minutos estuvo esperando?: "))
SubTotal = 2 + Kil + (0.5 * Tie_Esp)
Car_Noc = input("¿Fu un servicio de noche?: ")

if Car_Noc == "si":
    Recargo = SubTotal * 0.2
    Total = SubTotal + Recargo
    print(f"El recargo nocturno es: {Recargo} €")
else:
    Recargo = 0
    Total = SubTotal
    
print(f"El subtotal es: {SubTotal} €")
print(f"El total es: {Total} €")