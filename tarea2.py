'''
Isaac González 11-10396
Kervyn Rivero 11-10874
Equipo: Onesoft
Tarea 2'''

#############################################################################
#IMPORTO MODULOS
import calendar
from datetime import datetime
#############################################################################
#Clase
class Tarifa(object):
    def __init__(self):
        self.hs = 10.0
        self.hfs = 20.0

#############################################################################
def calcularPrecio (tarifa, tiempoDeTrabajo):
	#Hacer precondiciones
	#calculo tiempo de trabajo en dias y horas
	diferencia = tiempoDeTrabajo[0] - tiempoDeTrabajo[1]
	ndia = calendar.weekday(tiempoDeTrabajo[1].year, tiempoDeTrabajo[1].month, tiempoDeTrabajo[1].day)
	dia_i = tiempoDeTrabajo[1].day
	dia_f = tiempoDeTrabajo[0].day
	hora_i = tiempoDeTrabajo[1].hour
	print("DIA INICIAL: ",dia_i)
	print("DIA Final: ",dia_f)
	print("HORA INICIAL: ",hora_i)
	print("diferencia", diferencia.days)
	horas=0
	horasf=0
	horasx=0
	while ( dia_i < dia_f):
		#Si es fin de semana
		if (ndia==5 or ndia==6):
			while (hora_i < 24):
				horasf=horasf+1
				hora_i=hora_i+1

		#Sino
		else:
			while (hora_i < 24):
				horas=horas+1
				hora_i=hora_i+1
		hora_i=0
		dia_i = dia_i + 1
		print("DIA_TRABAJAR: ",dia_i)
		ndia = (ndia + 1) % 7

	#falta el ultimo dia. tengo que trabajar con los segundos.
	total=(horasf+horas)%24
	horasx=(((diferencia.seconds//60))//60)-total

	if (((diferencia.seconds//60)%60)>0):
		horasx=horasx+1

	if (ndia==5 or ndia==6):
		horasf = horasf + horasx

	else:
		horas = horas + horasx

	return horas,horasf


#############################################################################
tiempoDeTrabajo = [datetime(2016, 4, 23, 2, 0, 0), datetime(2016, 4, 22, 23, 0, 0)]
precios = Tarifa()
horas = calcularPrecio(precios,tiempoDeTrabajo)
print("Horas normales:",horas[0], "Horas especiales:",horas[1])