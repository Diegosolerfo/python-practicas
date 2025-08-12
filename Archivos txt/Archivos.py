#Open es para abrir el archivo ahi que igualarlo a algo para usarlo, y ahi se pone la ruta de donde esta
ar = open("Archivos txt\\archivo.txt", encoding="UTF-8") #El utf-8 es para leer los caracteres universalmente
#print(ar.read()) #comentado porque una vez que se abre no se puede volver a leer dos veces 
#Read es para leer el archivo 
#lineas = ar.readlines()
#resultado = ar.readline(10) #Esto lee los caracteres hasta que le digamos 10 caracteres en este caso
#resultado = ar.readline() #Para que lea solo una linea se deja vacio
#para cerrarlo se usa .close
ar.close()
print(ar)
