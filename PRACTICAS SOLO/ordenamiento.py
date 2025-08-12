#Cree el codigo para ordenar un arreglo de numeros
num = int(input("Num: "))
i=1
lista = []
for i in range(num):
    ele = int(input(f"Digite el valor {i+1}°: "))
    lista.append(ele)
final = []
for i in range(num):
    nume=min(lista)
    lista.remove(nume)
    final.append(nume)
    
print(lista)
print(final)

numeros = [10, 27, 62, 91, 72, 92, 61, 999, 10, 1, 87, 65, 772, 1000]
#Para obtener el numero maximo 

actual = 0
mas_grande = 0
for i in numeros:
    actual = i
    if actual >= mas_grande:
        mas_grande = actual
        
print(mas_grande)