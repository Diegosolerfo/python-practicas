#Crear una funcion que me imprima los numeros primos hasta un numero que le pasemos 
def primos(max):
    esprimo = False
    divisores = 1
    lista = []
    for i in range(max):
        if i == 2:
            esprimo = True
        elif i == 0 or i==1:
            continue
        if i%2 == 0:
            continue
        for j in range(i):
            
            if j==0 or j==1: 
                continue
            elif i%j == 0:
                divisores += 1
            elif divisores > 1:
                esprimo = False
                divisores = 1
                break
            elif divisores == 1:
                esprimo = True
        if esprimo == True:
            lista.append(i)
    
    return lista 

print(primos(900))