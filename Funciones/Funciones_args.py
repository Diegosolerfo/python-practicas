#Creando una funcion con args 
#El asterisco solo lo puede tener el ultimo paramtero no se puede poner mas 
def sumartodo(*numeros):
    return sum(numeros)
    
print(sumartodo(10,92,61))

#Creando una funcion con args 
def sumartodo(nombre, edad, numeros):
    numeros = sum([*numeros]) + edad
    retorno = (f"{nombre} Mira la suma de tu edad {edad} + los numeros es: {numeros}")
    
    return retorno
    
print(sumartodo("diego", 17, [19,7,9,1]))
