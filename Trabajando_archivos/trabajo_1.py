#Primero hacer el ciclo para recojer los datos
datos = []
for i in range(1,5):
    nombre = input(f"Ingrese nombre {i}: ")
    apellido = input(f"Ingrese apellido {i}: ")
    datos.append([nombre, apellido])
    
#Luego hacer el ciclo para escribir los datos en un archivo txt

with open("Trabajando_archivos\\archivo.txt", "w", encoding="UTF-8") as archivo:
    for dato in datos:
        archivo.write(f"{dato[0]} {dato[1]}\n")
    
#Optimizado
with open("Trabajando_archivos\\archivo.txt", "w") as archivo:
    archivo.writelines("Los nombres y apellidos son:\n")
    [archivo.writelines(f"Nombre: {n}     Apellido: {a}\n") for n,a in datos]
    