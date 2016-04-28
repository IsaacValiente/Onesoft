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
    def __init__(self,monto_normal=10.0,monto_especial=20.0):

        assert(monto_normal>=0 and monto_especial>=0 and monto_normal!=monto_especial),"Las tasas por hora no pueden ser negativas o iguales."
        self.hs = float(monto_normal)
        self.hfs = float(monto_especial)

#############################################################################
def calcularPrecio (tarifa, tiempoDeTrabajo):
    #Hacer precondiciones
    #calculo tiempo de trabajo en dias y horas
    diferencia = tiempoDeTrabajo[1] - tiempoDeTrabajo[0]
    assert(diferencia.days>=0 and diferencia.days <= 7 and (not (diferencia.days==0) or diferencia.seconds>=900)),"El tiempo trabajado total trabajado debe ser positivo,mayor a 15min y menor que 7 dias."
    ndia = calendar.weekday(tiempoDeTrabajo[0].year, tiempoDeTrabajo[0].month, tiempoDeTrabajo[0].day)
    dia_i = tiempoDeTrabajo[0].day
    dia_f = tiempoDeTrabajo[1].day
    hora_i = tiempoDeTrabajo[0].hour
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
        ndia = (ndia + 1) % 7

    #falta el ultimo dia. tengo que trabajar con los segundos.
    if (diferencia.days >0):
        diferencia=tiempoDeTrabajo[1]-(datetime(tiempoDeTrabajo[1].year, tiempoDeTrabajo[1].month, dia_f, 0, 0, 0))

    horasx=(((diferencia.seconds//60))//60)

    if (((diferencia.seconds//60)%60)>0):
        horasx=horasx+1

    if (ndia==5 or ndia==6):
        horasf = horasf + horasx

    else:
        horas = horas + horasx

    pago = tarifa.hs * horas + tarifa.hfs * horasf
    print("Horas normales:",horas, "Horas especiales:",horasf)
    return pago

#############################################################################
tiempoDeTrabajo = [datetime(2016, 4, 22, 23, 0, 0), datetime(2016, 4, 26, 0, 10, 0)]
precios = Tarifa(1, 2)
pago = calcularPrecio(precios,tiempoDeTrabajo)
print("Pago: ",pago,"bs")