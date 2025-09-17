#Para crear una funcion se necesita el def nombre()
#esa es la estructura de una funcion

def saludar():
    print("Hola a todos :)")
    
saludar()

#Ahora con parametros se usa asi
def saludar_dinamico(nombre, sexo):
    sexo = sexo.lower()
    if sexo == "hombre":
        adjetivo = "makina"
    elif sexo == "mujer":
        adjetivo = "berraca"
    else:
        adjetivo = "champion"
    print(f"Hola {nombre}, ¿como andas {adjetivo}?, ¿queres algo de comer?")
    
saludar_dinamico("Diego", "Hombre")
saludar_dinamico("Elizabeth","Mujer")
saludar_dinamico("Elefante", "Indefinido")

#Creando un afuncion con return, y puede retornar diferentes valores 
def crear_clave(num):
    carac = "abcdefjhijklmnñopqrstuvwxyz012345789"
    Entero = str(num)
    num = int(Entero[0])
    p1 = num + 3
    p2 = num -2
    p3 = num * 2
    p4 = num -7
    p5 = num + 9
    clave = (f"{carac[p1]}{carac[p2]}{carac[p3]}{carac[p4]}{carac[p5]}")
    return clave, num

clave, num = crear_clave(80)
print(f"El numero fue {num}, y la clave resultante es: {clave}")
