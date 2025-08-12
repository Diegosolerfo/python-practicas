#Vamos a usar contien para que siga con la siguiente ejecucion en caso de que se quiera omitir alguna cosa 

marcas = ["apple", "sansung", "oppo", "motorola", "hawei", "tecno"]

for marca in marcas: 
    if marca == "sansung": 
        continue
    elif marca == "oppo":
        break
    print(marca)

#contine es para que omita los demas y que continue con el recorrido
#break es para que el bucle se pare y no siga con el recorrido 


#Usando for en una cadena de texto 
cadena = "Diego Alejandro Soler"

for letra in cadena:
    print(letra)
    
#Usando for en una sola linea de texto

numeros = [2,3,4,5,6]

duplicados = [x*2 for x in numeros]
print(duplicados)