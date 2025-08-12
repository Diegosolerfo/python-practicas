#encontrando el numero mayor de una lista, tupla, conjunto, diccionario
numeros = {10,29,63,24,45,21,91,0,82,73}
num_max = max(numeros)

#encontrando el numero mas bajo de una lista, tupla, conjunto, diccionario
num_min = min(numeros)

#Redondeando decimales con round()

numero = 82.9183986124897987298648273
#print(round(numero,3))

#retorna false, -> false, 0, vacio, None
#Caso contrario si le damos un numero =! 0, o una cadena de string o una lista o tupla o algo con algun valor, o true

resultado_booleano = bool(0)

#all() retorna True en caso de que todos los valores sean True de un iterable

resultado_all = all([1,98, "hola", True, 1])

#sum() me va a sumar todos los numero de una lista o tupla 
Resul = sum(numeros)
print(Resul)