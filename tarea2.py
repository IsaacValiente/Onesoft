'''
Isaac González 11-10396
Kervyn Rivero 11-10874
Equipo: Onesoft
Tarea 2'''

#############################################################################
#IMPORTO MODULOS
from datetime import datetime
#############################################################################
#Clase
class Tarifa(object):
    def __init__(self):
        self.hs = 10.0
        self.hfs = 20.0

#############################################################################
def calcularPrecio (self,tarifa, tiempoDeTrabajo):
	#calculo tiempo de trabajo en dias y horas
	diferencia = tiempoDeTrabajo[0] - tiempoDeTrabajo[1]
	return


#############################################################################
tiempoDeTrabajo= [datetime.now(), datetime(2000, 11, 5, 22, 0, 0)]
diferencia = tiempoDeTrabajo[0] - tiempoDeTrabajo[1]
print("Fecha1:", tiempoDeTrabajo[0])
print("Fecha2:", tiempoDeTrabajo[1])
print("Diferencia:", diferencia)
print("Entre las 2 fechas hay ", diferencia.days, "días y ",\
 diferencia.seconds, "seg.")