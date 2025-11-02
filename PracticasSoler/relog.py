import time
from datetime import datetime as dt

def reloj():
    hora = dt.now()
    segundos, minutos, horas = hora.second, hora.minute, hora.hour
    while True:
        yield f"{horas:02}:{minutos:02}:{segundos:02}"
        segundos += 1
        if segundos == 60:
            segundos = 0
            minutos += 1
            if minutos == 60:
                minutos = 0
                horas += 1
                if horas == 60:
                    horas = 0
        time.sleep(1)

for hora_actual in reloj():
    print(hora_actual, end="\r", flush=True)

