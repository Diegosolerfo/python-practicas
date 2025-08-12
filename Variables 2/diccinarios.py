#Creando un diccinario con dict()

diccinario = dict(nombre="diego", apellido="soler", edad=17, Opcupacion="Programador profesional con 3 años de exp")

#print(diccinario)

#Las tuplas pueden ser claves de un diccionario
#Pero las listas no porque no son hasheables no son inmutables
#Las tuplas son inmutables y por eso son hasheables

diccionario_2 = {(1, 2): "Hola", (3, 4): "Mundo"}
#print(diccionario_2)

#Para meter conjuntos en un diccionario se hace asi
diccionario_3 = {frozenset({1, 2}): "Hola"}
#print(diccionario_3)

#Creando un diccinario con fromkeys(), nos deja todos los valores en none, pero tenenmos que pasarle las claves como una lista

diccionario_4 = dict.fromkeys(["nombre", "apellido"])
#Tambien se puede hacer asi
diccionario_4 = dict.fromkeys(["nombre", "apellido"], "desconocido")

print(diccionario_4)

