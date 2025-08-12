#Vamos a ejecutar una funcion para que no permita que el usuario cometa errares o que no genere excepciones osea
#las vamos a controlar
def sumar():
    #Es un bucle infinito, hasta que funcione
    while True:
        a = input("Ingrese un numero: ")
        b = input("Ingrese otro numero: ")
        #try es para intentar hacer algo, si no se puede hacer, se va a except
        try:
            return int(a) + int(b)
        #except es para que si hay una excepcion, se ejecute algo y no pare el programa
        #e es la excepcion que nos esta dando
        #Dentro de las expeciones exiten muchas excepciones, como ValueError, TypeError, etc
        except Exception as e:
            print(f"Che, pedazo de inutil, te dije que numeros\nmira lo queprovocaste: {e}")
            #para ver el nombre de la excepcion es asi: 
            print(f"ERROR: {type(e).__name__}")
        #else se ejecuta si no hay excepciones
        else: 
            break
        #Esto se ejecuat siempre sin importar que pase no tiene mucho uso pero a veces si 
        finally:
            print("Se ejecuta siempre")
            
print(sumar())