#Nómina de empleado
# Calcula el salario neto de un trabajador:
#Entradas: salario base mensual, número de horas extra 
# (pagadas a 1,5× el valor de la hora normal), porcentaje de retención de IRPF, 
# porcentaje de seguridad social.
#Salida: salario bruto, importe de IRPF, 
#importe de seguridad social y salario neto.

#Datos a tener en cuenta:
# - Importe IPRF: 15%
# - Importe Seguridad Social: 6%

# Pasos a seguir:
# 1. Definir variables necesarias y pedir al usuario los datos necesarios
print("Binvenido a la calculadora de la nomina, porfavor ingrese su salrario en Euros")
SalBas = float(input("Ingrese el salario Base Mensual: "))
HorasEx = int(input("Ingrese las horas extra trabajadas: "))
# 2. Cacular: salario bruto = SalBas + Horas Ex, IRPF = SalBruto * 0.15, SS = SalBruto * 0.06, Salario neto = SalBas - IRPF - SegSoc, 
Valor_Hora = SalBas / 160
Hora_Extras = (Valor_Hora * 1.5) * HorasEx
SalBruto = SalBas + Hora_Extras
IRPF = SalBruto * 0.15
Seg_Soc = SalBruto * 0.06
Sal_Neto = SalBruto - IRPF - Seg_Soc
# 3. Imprimir los resultados y ya :)
print("Los resultados son los siguientes:")
print(f"Pago horas extra: {Hora_Extras:.2f} €")
print(f"El salario bruto es: {SalBruto:.2f} €")
print(f"El importe de IRPF es: {IRPF:.2f} €")
print(f"El importe de Seguridad Social es: {Seg_Soc:.2f} €")
print(f"El salario neto es: {Sal_Neto:.2f} €")
print("Gracias por usar la calculadora de nomina")