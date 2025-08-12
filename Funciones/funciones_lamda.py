#Creando un afuncion lambda, oesa una funcon anonima sin nombre, no se abre un bloque de istrucciones para esto solo
#se puede guaradar en una variable

multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos)

#Usando lambda y filter para definir una lista de numeros si son par o inpar
numerosb = [1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,120,172,81,27,39,47]
pares = filter(lambda numeros:numeros%2 == 0, numerosb)
print(list(pares))
impares = filter(lambda numeros:numeros%2 == 1, numerosb)
print(list(impares))
#Lo que hace la funcion filter es que le pasamos una funcion y una lista y valor por valor nos devolvera true y se guadare en el variable 
#si cumple con el proceso requerido para ser True es com un bucle en menos lineas de codigo 

#Otro ejemplo
gente = {
    "diego": "M",
    "valerie": "F",
    "pilar": "F", 
    "pedro": "M",
    "danna": "F",
    "johao": "M"
}

hombres = filter(lambda persona: gente[persona] == "M", gente)
print(f"Los hombres somos: {list(hombres)}")

Mujeres = filter(lambda persona: gente[persona] == "F", gente)
print(f"Las mujeres son: {list(Mujeres)}")