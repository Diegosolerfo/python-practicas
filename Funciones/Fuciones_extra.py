#Creando una funcion con parametros normal

def saludo(nombre, edad, caracteristica):
    frase = (f"Hola {nombre}, tenes {edad}?, bua tenes una banda por delante {caracteristica}")
    return frase

print(saludo("diego", 17, "sapo"))
#Creando una funcion con parametros predefinidos

def saludo(nombre="pedro", edad=71, caracteristica="capo"):
    frase = (f"Hola {nombre}, tenes {edad}?, bua tenes una banda por delante {caracteristica}")
    return frase

print(saludo("diego"))

