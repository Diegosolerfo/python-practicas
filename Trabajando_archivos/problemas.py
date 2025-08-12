#Cambiar el tipo de dato de una columna en un archivo csv
import pandas as pd
data = pd.read_csv('Trabajando_archivos\\tabla.csv')
data["Edad"] = data["Edad"].astype(str)
print(data.loc[:,["Edad"]])
#Remplazar un valor por otro con replace

data["Nombre"].replace("Danna","Dana",inplace=True)



#Para eliminarc filas incompletas se usa dropna
data = data.dropna()
#print(data)
#Y si se necesita elimar columnas con datos faltantes se usa axis=1 en el ()


#Eliminando filas repetidas
data = data.drop_duplicates()

#Creando un archivo cvs y dejando el data resultante

data.to_csv('Trabajando_archivos\\tabla_2.csv')

print(data)