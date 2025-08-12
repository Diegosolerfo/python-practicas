import Calculadora.normales as nor, Calculadora.avanzadas as ava
import Presentacion.Saludos as sal, Presentacion.Despedidas as des

def menu():
    opciones = sal.saludar()
    print (opciones)
    opcion = int(input("Ingrese el valor que desea ejecutar: "))
    if opcion == 1:
        val1 = int(input("Ingrese el valor 1: "))
        val2 = int(input("Ingrese el valor 2: "))
        resultado = nor.sumar(val1, val2)
    elif opcion == 2:
        val1 = int(input("Ingrese el valor 1: "))
        val2 = int(input("Ingrese el valor 2: "))
        resultado = nor.restar(val1, val2)
    elif opcion == 3: #Multiplicacion
        val1 = int(input("Ingrese el valor 1: "))
        val2 = int(input("Ingrese el valor 2: "))
        resultado = nor.multiplicar(val1, val2)
    elif opcion == 4: #division
        val1 = int(input("Ingrese el valor 1: "))
        val2 = int(input("Ingrese el valor 2: "))
        resultado = nor.dividir(val1, val2)
    elif opcion == 5: #potenciacion
        val1 = int(input("Ingrese el valor 1: "))
        val2 = int(input("Ingrese el valor 2: "))
        resultado = ava.pot(val1, val2)
    elif opcion == 6: # raiz
        val1 = int(input("Ingrese el valor: "))
        resultado = ava.raiz(val1)
    elif opcion == 7: #locaritmacion
        val1 = int(input("Ingrese el valor 1: "))
        val2 = int(input("Ingrese el valor 2: "))
        resultado = ava.log(val1, val2)
    else: 
        val = des.Adios()
    return resultado

ejecutarse = "si"

while ejecutarse == "si":
    inicio = menu()
    print(inicio)
    ejecutarse = input("desea que el programa se ejecute otra vez?: ")
    
print(des.parece())