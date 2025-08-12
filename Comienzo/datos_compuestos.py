#Estos datos estan com´puestos de otros datos simples o compuetos 
#Lista se pueden modificar los datos
lista = ["Diego Soler", "Hola mundo", 17, "1.80", "H"]
#print(lista[3])

#Tupla nunca se va a modificar 
tupla = ("Diego Soler", "Hola mundo", 17, "1.80", "H")

#print(tupla[3])

#conjuntos
#Es aquel en el que no se pueden modificar los datos pero se puede redefinir el conjunto
#No se pueden repetir los datos
#No se puede acceder a los datos por medio de indices
conjunto = {"Diego Soler", "Hola mundo", 17, "1.80", "H"}


#diccionarios o jasons jjajaja
#Es un conjunto de datos compuestos por clave y valor
#No se pueden repetir las claves
#Se pueden modificar los datos
diccionario = {
    "nombre":"Diego Soler", 
    "mensaje":"Hola mundo", 
    "edad":17, 
    "estatura":"1.80", 
    1:"H"
}

print(diccionario["nombre"])