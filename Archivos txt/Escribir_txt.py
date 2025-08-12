with open("Archivos txt\\archivo.txt","w",encoding="UTF-8") as archivo:
    #Esto sirve para sobreescribir el archivo de texto
    #Write nos pide un str no una lista
    #archivo.write("Hola sapa espero que hay aservido esta mrd.")
    #witelines() nos pide una lista de caracteres para color ahi y escribirla 
    archivo.writelines(["Hola que buena no?","interesante esta joda \n","queria ver que sapsa con esa backslash y n"])
    #agergando texto con una sola linea de codigo pa y con un for
    for i in range(5): archivo.write(f"\nlinea {i} agregada correctamente")
    