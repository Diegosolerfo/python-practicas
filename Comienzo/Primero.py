#Hacer un programa para agendar citas medicas facil y rapido 
#El programa debe utilizxar las variables que son los datos del paciente los datos del medico y la fecha lugar y hora de la cita 

Usuario = {
    "Nombre":  "Pedro Jose",
    "Edad": 43,
    "Nacionalidad": "Colombiana",
    "Cedula": 123456789,
    "Telefono": 1234567890,
    "Correo": "pedro@gmail.com"
}

Medico = {
    "Nombre": "Juan Carlos",
    "Especialidad": "Medicina General",
    "Telefono": 1234567890,
    "Correo": "doctorcaraculo@hotmail.com"
}

print("Agende su cita medica con anticipacion")
dia= input("Ingrese el dia de la cita: ")
hora = input("Ingrese la hora de la cita: ")
lugares = {
    "Hospital":True, 
    "Casa":False, 
    "Hospital 2":True, 
    "Consultorio alternativo":True, 
    "Otro":False
}
def validar_lugar(lugar):
    if lugar in lugares:
        if lugares[lugar] == True:
            return True
    else:
        return False

lugar = input("Ingrese el lugar de la cita: ")
lugar = validar_lugar(lugar)
agendada = False

while agendada == False:
    if lugar == True:
        print("Su cita esta agendada para el dia " + dia + " a las " + hora + " en " + lugar)
        agendada = True
    else:
        print("No se puede agendar la cita, por favor ingrese un lugar valido")
        lugar = input("Ingrese otro lugar para la cita: ")
    
print("Su cita esta agendada para el dia " + dia + " a las " + hora + " en " + lugar)
print("Datos del paciente: ")
print(Usuario)
print("Datos del medico: ")
