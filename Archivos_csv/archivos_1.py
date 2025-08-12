#Importamos el modulo para leer archivos csv
import csv

with open("Archivos_csv\\tabla.csv", encoding="UTF-8") as archivo:
    #Leyendo el archivos con una funcion de el modulo de csv
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)


#AUNQUE ESTO NO ES LO MEJOR, PROFESIONALMENTE SE DEBERIA LEER CON PANDAS PORQUE... VAYA PANDAS