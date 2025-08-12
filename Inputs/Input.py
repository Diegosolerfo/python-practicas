#Pedirle un dato a el usuario

nombre = input("Dame tu nombre: ")
con = nombre.isnumeric()
if con:
    print("Eso no es un nombre, hazlo otra vez")
else:
    print("hola " + nombre) 

AñosTrabajando = input("¿Cuantos años llevas trabajando?: ")
Salario = input("¿Cual es tu salario? ")
S=int(Salario)
AT=int(AñosTrabajando)

if AT > 4:
    print("Felicidades, tienes un aumento:")
    print(f"Tu nuevo salario es de: {int(S*2)}")
else:
    print("Sigue trabajando duro")
    