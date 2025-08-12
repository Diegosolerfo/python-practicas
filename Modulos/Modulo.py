#Se puede renombrar el modula usando as 
import Modul as m

sapa  = m.despedirse("Pedro")
print(sapa)
#Para no hacer referencia o llamar a un namespace se ´puede hacer esto: 

from Modul import despedirse, saludar_bien
c1 = despedirse("Diego")
print(c1)
c2 = saludar_bien("Sapa")
print(c2)

#Para acceder a una carpeta que esta adentro de otra carpeta en el la misma carpeta Osea:
#Capeta
#   archivo (actual)
#   carpeta

#seria asi: Primero va el nombre de la carpeta y despues el del archivo u  otra carpeta si es el caso 

import Modulos_1.Modulos_dentro as Modulos
#Y para una carpeta o archivo que esta afuera del archivop actual se accede asi:
import sys
print(sys.path)
sys.path.append("C:\\Users\\USUARIO\\OneDrive\\Desktop\\PRUEBAS PYTHON\\Funciones")

#import Bulf_in as bo

#print(bo.resultado_booleano)

#Tira un error pero nah no pasa nada perro