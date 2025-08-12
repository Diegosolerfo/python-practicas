#Creando un funcion que muestre la serie fibonacci 

def fibonacci(num):
    lista = []
    dato1, dato2 = 0, 1
    for i in range(num):
        if dato2+dato1 > num:
            break
        lista.append(dato1 + dato2)
        dato1 = dato2
        dato2 = lista[i]
        
    return lista

numeros = fibonacci(20)
print(numeros)
