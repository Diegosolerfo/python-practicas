#El bucla for recorrera (iterara) en funcion de los elementos que tenga el dato que le pasemos por ejempolo=

#Recorriendo una conjunto
animales = {"perro", "gato", "cuerpoespin", "loro", "tuputamadre"}

#for animal in animales:
#    print(f"El animal al que es igual animal es: {animal}")

#Otro ejemplo

numeros = {10, 16, 82, 4, 92}

#for numero in numeros:
#    print(f"el numero en esta iteracion es {numero}")

#Asi se pueden recorrer dos conjuntos al mismo tiempo se puede con mas usando el mismo formato de abajo

#for animal, numero in zip(animales, numeros):
#    print(f"El animal es conjunto 1 es: {animal}")   
#    print(f"El numero en conjunto 2 es: {numero}")

#Otra funcion para for es range() que nos permite iterar con un rango por ejemplo (5,10) el primer numero es desde 
#donde empieza y el segundo es hasta cuando menos uno, y si solo le pasamos uno (10) lo que hara es imprimir eso 
#desde el 0 hasta el numero que le digamos menos uno 

#for num in range(10,16):
#    print(num)

#Y asi se puede recorrer en indices para las conjuntos 0, 1 ,2 3,4 5, ....
#Recordad que len() nos da la longitud de la conjunto o cuantos elementos tiene
    
#La forma correcta de hacer esto es con la funcion enumerate() que nos devuelve una tupla con el indice y el valor
#de la conjunto

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"Indice [{indice}] - Valor [{valor}]")
    
#Reto desempaquetar la tupla directamente en el for
numeros = list([])
for num, i in enumerate(numeros):
    #Lo que esta pasando aqui es que en num se guarda el indice y en i se guarda el valor de la conjunto osea desempaquetamos la tupla
    print(f"Indice [{num}] - Valor [{i}]")
#Se puede hacer que el else sirva para ver si no hay elementos por recorrer y se ejecutara siempre 
#Importante si ahi un break en el for no se ejecutara el else 
else:    
    print("No hay mas elementos por recorrer")
    
#Todo esto funciona exctamente igual para las tuplas y conjuntos 