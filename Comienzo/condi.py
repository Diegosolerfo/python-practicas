edad = 43
nombre = "pedro jose"
nacionalidad = "Colombiana"

if edad >= 18:
    print(nombre + " Es mayor de edad")
    if nacionalidad == "Colombiano" or nacionalidad == "Colombiana":
        print("Puedes beber licor chimba")
    
    elif nacionalidad == "Estadounidense": 
        print("No puedes beber licor por tu nacionalidad")
    else: 
        print("No se puede determinar la nacionalidad")
else:
    print(nombre + " Es menor de edad, y no puede beber alcohol")
    