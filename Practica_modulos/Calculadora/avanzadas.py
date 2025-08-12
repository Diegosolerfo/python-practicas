def pot(a, b):
    c=0
    anterior = 0
    for i in range(1,b):
        if i == 1:
            anterior = a * a
            if b==2:
                return anterior
        else:
            anterior = anterior * a
            c=anterior
    return c

def raiz(a):
    resultado = 2
    aux = 0
    con = 0
    while con != 1:
        aux = resultado
        resultado *= resultado
        if(resultado == a):
            break
        elif(resultado > 10000):
            return ("No tiene raiz exacta")
            break
        else:
            resultado = aux + 1
    return aux
# a, b --- a = la base, b = el final, c = la cantidad de veces que debe multiplicarse          
def log(a, b):
    c = 0
    aux = 0
    while aux != b:
        aux = pot(a, c)
        c+=1
        if c>1000:
            return f"El locaritmo base {a} de {b} no es exacto"
            break
            
    return c-1