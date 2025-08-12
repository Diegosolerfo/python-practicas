#Los diccionarios funcionan diferente 

diccionario = {
    "nombre": "diego",
    "apellido": "soler",
    "edad": 17,
    "direccion": "Cra 126 D 132 D N 64",
    "lugar_favorito": "El parque fontanar",
    "Aspiraciones": "Ser un programador profesional"
}
#Asi se obtienen solo las claves sin los valores de un diccionario recoriendolo en un bucle for

for key in diccionario:
    print(key)

#Asi se recorre un diccionario con el indice o clave y el valor
for key, val in diccionario.items():
    print(f"{key} {val}")