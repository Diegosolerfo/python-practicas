import pandas as pd
#Promero buscamos el archivo asi: 
archivo  = pd.read_csv("Archivos_csv\\tabla.csv")
archivo2 = pd.read_csv("Archivos_csv\\tabla.csv")

#Esa variable archivo es un df dataframe que es un tipo de archvio bidimencional con 
#filas y columnas

#Obteniendo los datos de la columna nombre 
#print(archivo["Nombre"])

#Ordenando los datos por la edad
ordenado = archivo.sort_values("Nombre")

#Ordenandolo de forma desendente 
ordenado_desendente = archivo.sort_values("Apellido",ascending=False)

#He aqui un entreparentesis (jupiternotebook se usa mucho para ciencia de datos y para inteligencia artificial)

#Concatenando los dataframes con concat() que es para eso se le tiene que pasar una lista con lo que se quiera concatenar 
archivo3 = pd.concat([archivo, archivo2])

#accediendo a las primeras dilas con head()
primerasfilas = archivo3.head(2)
#print(primerasfilas)

#accediendo a las ultimas filas con tail()
ultimasfilas = archivo3.tail(2)
#print(ultimasfilas)

#accediendo a la cantidad de filas y columnas con shape
#Esto lo que nos tira es una tupla con la cantidad de filas y columnas
#Por ejemplo si tenemos 3 filas y 2 columnas nos tira (3,2) primeros las filas luego las columnas 
cantidad = archivo.shape
#desempaquetando
filas, columnas = archivo.shape

#describe() nos tira un resumen de los datos
resumen = archivo.describe()

#accediendo a un elemento espedifico con loc()
#loc() recibe dos parametros el primero es la fila y el segundo la columna
elemento = archivo.loc[0,"Nombre"]
#iloc() es lomismo pero con los indices poreso la i
elemento2 = archivo.iloc[1,0]

#accediendo a tola las filas de una columna
datos = archivo.loc[:,"Nombre"]
#iloc() es lomismo pero con los indices poreso la i
datos2 = archivo.iloc[:,0]

#ahora las columnas de una fila osea un registro para que lo entienda
dates = archivo.loc[0,:]

#accediendo a filas con edad mayor que 20
mayores = archivo.loc[archivo["Edad"]>20,:]

print(mayores)