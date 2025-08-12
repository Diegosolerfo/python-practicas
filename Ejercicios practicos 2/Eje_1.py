#Pedir los datos de los estudiantes, nombre y edad
#Utilizare un for para rellenar un diccionario 

estudiantes = dict({})
cantidad_estudiantes = int(input("¿Cuantos estudiantes son?: "))
for i in range(cantidad_estudiantes):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    estudiantes[nombre] = edad
    
#Ordenar los datos de menor a mayor
#funcion para encontrar al menor estudiante del diccionario
def menorest(listado):
    menor = float('inf')
    nombre = ""
    for nom, eda in listado.items():
        if eda <= menor:
            nombre = nom 
            menor = eda
    return nombre, menor
#funcion para elcontrar el mayor de un estudiante en el diccionario
def mayorest(listado):
    mayor = float('-inf')
    nombre = ""
    for nom, eda in listado.items():
        if eda > mayor:
            nombre = nom 
            mayor = eda
    return nombre, mayor

est_ordenados = dict({})
while estudiantes:
    nom, eda = menorest(estudiantes)
    est_ordenados[nom] = eda 
    estudiantes.pop(nom)
    
#Mensacionar quien es el alumno profesor y quien es el asistente profesor el mayor y el asistente es el menor

profesor, edapro = mayorest(est_ordenados)
asistente, edaasi = menorest(est_ordenados)
print("Lista de estudiantes ordenada de menor a mayor")
i=1
for nom, eda in est_ordenados.items():
    print(f"{i}.) {nom} con {eda} años")
    i+=1
    
print(f"El profesor es: {profesor} por el ser el mayor con {edapro}")
print(f"El asistente es: {asistente} por el ser el menor con {edaasi}")