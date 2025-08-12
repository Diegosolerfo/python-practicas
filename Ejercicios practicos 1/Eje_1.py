#Datos

HDalto = 1.5
HcPromedio = 4
HcMax = 7
HcMin = 2.5

#Diferencias de duracion de cursos en comparacion con el de dalto

Dif1 = 100 - HDalto / HcPromedio * 100
Dif2 = 100 - HDalto*1000 // HcMax / 10
Dif3 = 100 - HDalto / HcMin * 100
print("------------------------------------------------------------")
print(f"El curso de dalto fue un {Dif1}% mas rapido que el promedio")
print(f"El curso de dalto fue un {Dif2}% mas rapido que el mas largo")
print(f"El curso de dalto fue un {Dif3}% mas rapido que el mas corto")

#Mas vaiables 

CrudoD = 3.5
CrudoP = 5

#Porcentaje para el crudo
Pro1 = 100 - HDalto*1000 // CrudoD / 10
Pro2 = 100 - HcPromedio*1000 // CrudoP / 10

print("------------------------------------------------------------")
print(f"El porcentaje removido de dalto fue un {Pro1}%")
print(f"De otros cursos el porcentaje removido fue de {Pro2}%")    



#Mostrar la cantidad de horas equivalentes a las de un curso en comparacion a dalto

#Calculando las horas equivalentes
Ca1 = 10*HcPromedio*100 // HDalto /100
Ca2 = 10*HcMax*100 // HDalto /100
Ca3 = 10*HcMin*100 // HDalto /100

print("------------------------------------------------------------")
print(f"Un curso de dalto es equivalente a {Ca1} horas de un curso promedio")
print(f"Un curso de dalto es equivalente a {Ca2} horas de un curso largo")
print(f"Un curso de dalto es equivalente a {Ca3} horas de un curso corto")
print("------------------------------------------------------------")
print(f"Y ver 10 horas de otros cursos equivale a ver {10*HDalto / HcPromedio} horas de dalto")
print("------------------------------------------------------------")