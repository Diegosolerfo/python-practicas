#Creando un conjunto con set()

conjunto = set([1, 2, 3, 4, 5])

print(conjunto)

#Para meter un conjunto dentro de otro conjunto se hace asi

conjunto_1 = frozenset([1, 2, 3, 4, 5])
conjunto_2 = {conjunto_1, 6, 7, 8, 9}

print(conjunto_2)

#Teoria de conjuntos :)

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 2}
#Verifiicando si un conjunto es un subconjunto de otro
#resultado = conjunto2.issubset(conjunto1)
#Tambien se puede usar <=
resultado = conjunto2 <= conjunto1

#verificando que un conjunto sea un superconjunto de otro
resultado = conjunto1.issuperset(conjunto2)
#Tambien se puede usar >=
resultado = conjunto1 >= conjunto2

#Verificando si tiene dos datos en común 
resultado = conjunto1.isdisjoint(conjunto2)
#Asi imprime false pero
conjunto3 = {6, 7, 8} 
resultado = conjunto1.isdisjoint(conjunto2)

print(resultado)