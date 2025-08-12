# Lo mismo pero mas barato ;) consume menos recursos es mas optimo entonces 10/10
with open("Archivos txt\\archivo.txt", encoding="UTF-8") as archivo:
    # aIgualando el archivo y leyendolo a una variable para utlizxarlo en el bloqque de instrucciones 
    archivo_leido = archivo.read()
    print(archivo_leido)
    #No es necesario cerrarlo porque se cierra automaticamente ya que es un bloque de instrucciones