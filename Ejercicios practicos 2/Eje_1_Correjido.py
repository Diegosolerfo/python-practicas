#hacer un rpograma para ordenar unos estudiantes del menor al mayor y el mayor es el profe y el menor es el asistente
def obt_alu(cantidad):
    compañeros = []
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del estudiante: ") 
        edad = int(input("Ingrese la edad del estudiante: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key = lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return profesor, asistente, compañeros

estudiantes = 4
pro,asi,com = obt_alu(estudiantes)
print(f"El profesor es {pro} y su asistente es {asi} Y la lista en orden asendente es: {com}")

