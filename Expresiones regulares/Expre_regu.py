import re 

texto = """Hola sapa como vas?, yo bien gracias ya casi termi.no el 1er curso de python de dalto mk que gono a antes de las 8
        -a boludo que bueno que sos che
        -no hijo .de puta mer estas superando
        -si enfermo de mierda muere   89.  boludo
        -me las pelas sapa perra vopy a alzanzarte
        -no lo creo bOlUdo ababababababaab
"""
#el metodo findall busca todas las coincidencias de la palabra boludo
#el metodo search busca la primera coincidencia de la palabra boludo
#flags = re.IGNORECASE busca la palabra boludo sin importar si esta en mayuscula o minuscula
#resltado = re.findall("boludo", texto, flags= re.IGNORECASE)

#Empezando con las expresiones regulares 
#\d busca cualquier digito del 0 al 9
#lo que hace la r es como lo que hace la f(fstrings) pues la "r" indica que es una expresion regular
#resultado = re.findall(r"\d", texto)
#\D busca TODO menos los digitos del 0 al 9
#resultado = re.findall(r"\D", texto)


#---------------------------------------------------

#\w busca caracteres alfanumericos y guiones bajos 
#resultado = re.findall(r"\w", texto)
#\W busca todo menos caracteres alfanumericos y guiones bajos
#resultado = re.findall(r"\W", texto)

#---------------------------------------------------

#\s busca espacios en blanco, tabs, saltos de linea
#resultado = re.findall(r"\s", texto)
#\S busca todo menos espacios en blanco
#resultado = re.findall(r"\S", texto)

#---------------------------------------------------
#. busca cualquier caracter menos el salto de linea
#resultado = re.findall(r".", texto)
#\n busca todos los saltos de linea
#resultado = re.findall(r"\n", texto)

#---------------------------------------------------

#\ cancela caracteres especiales, cancelar la funcion del punto y buscar el punto como cacacter
#resultado = re.findall(r"\.", texto)

#---------------------------------------------------

#Ahora vamos a buscar una cadena que tenga numero - punto - espacio
#resultado = re.findall(f"\d\.\s",texto)

#---------------------------------------------------

#^ busca el inicio de una cadena
#y si usamos re.M lo hace multilinea en los parametrso de flags
#resultado = re.findall(r"^        -a", texto, flags=re.M)

#---------------------------------------------------

# $ busca el final de una cadena
#resultado = re.findall(r"boludo$", texto, flags= re.M)

#---------------------------------------------------

#\d busca los digitos y si le ponemos {n} busca n cantidad de digitos
#resultado = re.findall(r"\d{2}\.", texto)

#{n,m} es para minimo y maximo de digitos
#resultado = re.findall(r"\d{1,4}", texto)

#---------------------------------------------------

#[] busca los caracteres que esten dentro de los corchetes
#resultado = re.findall(r"(ab){1}", texto)

#---------------------------------------------------

#El operador | busca una palabra u otra
resultado = re.findall(r"boludo|sapa", texto)
print(resultado)

#EN FIN EXPRESIONES REGULARES ES UN TEMA MUY AMPLIO Y COMPLEJO, PERO CON PRACTICA SE PUEDE DOMINAR
#Y ES MUY UTIL PARA BUSCAR PATRONES EN UN TEXTO

#SI NECESITA ALGO DE ESTO SOLO ES BUSCAR EN INTERNET, HAY MUCHA INFORMACION SOBRE ESTO
#Y HAY PAGINAS QUE TE AYUDAN A CREAR TU EXPRESION REGULAR