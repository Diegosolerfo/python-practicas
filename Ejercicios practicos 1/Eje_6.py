import string

# Pidiendo el texto al usuario
texto = input("Escribe el texto que quieras: ")

# Convertir el texto a minúsculas y eliminar signos de puntuación
texto = texto.lower().translate(str.maketrans('', '', string.punctuation))

# Proceso 1: Contar la frecuencia de cada palabra
palabras = texto.split()
frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Imprimir el diccionario con las frecuencias de las palabras
for palabra, frecuencia in frecuencia_palabras.items():
    print(f"{palabra}: {frecuencia}")