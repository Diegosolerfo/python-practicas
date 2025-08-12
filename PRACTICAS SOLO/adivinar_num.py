import random as rd

def adivinar_numero():
    numero_ad = rd.randint(1,100)
    n_intentos = 0
    intento = 0
    while True:
        try:
            intento = int(input(f"Intento N°{n_intentos+1}:"))
            if intento < 1 or intento > 100:
                continue
            n_intentos += 1
        except:
            print("Ingrese un valor valido, es decir un numero del 1 al 100")
            n_intentos += 1
        if intento < numero_ad:
            mensaje = "El numero es mayor"
        elif intento > numero_ad:
            mensaje = "El numero es menor"
        else:
            mensaje = "Felicidades, adivinaste el numero"
        print(mensaje)
        if intento == numero_ad:
            mensaje = f"Me leiste la mente capo si era el {numero_ad} y lo adivinaste en {n_intentos} intentos"
            break
        
    return mensaje
    

print(adivinar_numero())