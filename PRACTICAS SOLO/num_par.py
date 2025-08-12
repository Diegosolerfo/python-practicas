#primero pedimos el numero al usuario

while True:
    try:
        numero = int(input("Ingrese un numero:"))
    except:
        print("Porfavor un numero entero")
    else:
        break

if numero % 2 == 0:
    print("El numero es par")
else:
    print("el numero es impar")