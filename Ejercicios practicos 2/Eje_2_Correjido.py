#Creando una funcion para determinar si un numero es primo 

def es_primo(num):
    for i in range(2,num-1):
        if num%i == 0:
            return False
    return True

def lista(max):
    primos = []
    for i in range(2,max+1):
        valor = es_primo(i)
        if valor == True:
            primos.append(i)
    return primos

listas = lista(13)
print(listas)