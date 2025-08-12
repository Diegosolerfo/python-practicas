#Programa que cuente cuantas consonantes tiene un texto dado por el usuario

#Datos
texto = input("Dime un texto: ")
texto = texto.lower()
Consonantes = 0
Vocales = 0
#Proceso
for letra in texto:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        Vocales += 1
    elif letra == " ":
        pass
    else:
        Consonantes += 1
        
#Salida
print(f"El texto tiene {Consonantes} consonantes y {Vocales} vocales")