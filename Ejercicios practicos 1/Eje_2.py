# Calcular el tiempo que se toma una persona en decir unas cuantas palabras tendiendo en cuanta que se demorq 1 segundo en decir 2 palabras
Frase = input("Dime una frase: ")
Palabras = Frase.split(" ")
Cantidad = len(Palabras)
Tiempo = Cantidad/2

if Tiempo>60:
    print(f"Che flaco no me recagues de texto te pedi una frase no una testamento que te pensas que soy un robot, te tomas {Tiempo} segundos para decir la frase de {Cantidad} palabras")
else: 
    print(f"Che flaco te tomas {Tiempo} segundos para decir la frase de {Cantidad} palabras")
    
print(f"A dalto le tomaria cerca de {(Tiempo*1.3)} segundos en decir esas boludeses")