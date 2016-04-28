###########################################
##                 TAREA 2               ##
###########################################
#										  #
#	INTEGRANTES:						  #
#										  #
#		Kervyn Rivero: 11-10874			  #
#		Isaac Gonzalez: 11-10396     	  #
#										  #
###########################################
import unitest
from tarea import *
import calendar
from datetime import datetime

class tareaTester(unittest.TestCase):

							#################################
							##       Pruebas unitarias     ##
							#################################

	def testTasaIgual(self):
	# tasas Distintas
		a=3
		b=a
		aTasas=(a,b)
		assert(a!=b, "Las tasas no pueden ser iguales")						
	def testMinMInutos(self):
		# Minimo de minutos que debe trabajar una persona para facturar
		precios = Tarifa(1, 2)
		tiempoDeTrabajo = [datetime(2016, 4, 22, 23, 0, 0), datetime(2016, 4, 23, 23, 10, 0)]
		pago = calcularPrecio(precios,tiempoDeTrabajo)
    	diferencia = tiempoDeTrabajo[1] - tiempoDeTrabajo[0]
		assert((diferencia.days==0 and  and diferencia.seconds>=900), "El tiempo tiene que ser mayor o igual a 15min")

	def testMaxDias(self):
		# Prueba que verifica el maximo de dias que puede trabajar  una persona
		precios = Tarifa(1, 2)
		tiempoDeTrabajo = [datetime(2016, 4, 15, 23, 0, 0), datetime(2016, 4, 23, 23, 10, 0)]
		pago = calcularPrecio(precios,tiempoDeTrabajo)
		diferencia = tiempoDeTrabajo[1] - tiempoDeTrabajo[0]
		assert(diferencia.days<=7, "Los dias tienen que ser menor o igual a 7")
	def testFakeDateString(self):
		# Prueba que verifica el tipo de datos de las fechas
		precios = Tarifa(1, 2)
		tiempoDeTrabajo = [datetime(2016, 'a', 15, 23, 0, 0), datetime(2016, 4, 23, 23, 10, 0)]
		pago = calcularPrecio(precios,tiempoDeTrabajo)
		assert((isinstance(tiempoDeTrabajo[1].day, int) and isinstance(tiempoDeTrabajo[1].month, int) and isinstance(tiempoDeTrabajo[1].year, int)), "Los dias tienen que ser menor o igual a 7")

	def testFakeDataNegative(self):
	# Prueba que verifica el tipo de datos de las fechas
		precios = Tarifa(1, 2)
		tiempoDeTrabajo = [datetime(2016, -4, 15, 23, 0, 0), datetime(2016, 4, 23, 23, 10, 0)]
		pago = calcularPrecio(precios,tiempoDeTrabajo)
		assert(tiempoDeTrabajo[0].day>=0 and tiempoDeTrabajo[0].month>=0 and tiempoDeTrabajo[0].year>=0, "No se aceptan numeros negativos")

							###########################################
							##          Pruebas de aceptacion        ##
							###########################################

	
	def testHoraSalidamasTemprano(self):
	# Prueba que verifica el orden de las horas
		precios = Tarifa(1, 2)
		tiempoDeTrabajo = [datetime(2016, 4, 22, 23, 0, 0), datetime(2016, 4, 20, 23, 10, 0)]
		pago = calcularPrecio(precios,tiempoDeTrabajo)
		assert((tiempoDeTrabajo[1].day - tiempoDeTrabajo[0].day)>=0, "Los dias tienen que estar en el orden correcto")


	def testHorasiguales(self):
	# Horas iguales
		precios = Tarifa(1, 2)
		tiempoDeTrabajo = [datetime(2016, 4, 22, 23, 0, 0), datetime(2016, 4, 22, 23, 0, 0)]
		pago = calcularPrecio(precios,tiempoDeTrabajo)
		diferencia = tiempoDeTrabajo[1] - tiempoDeTrabajo[0]
		assert((diferencia.days==0 and  and diferencia.seconds>=900), "El tiempo tiene que ser mayor o igual a 15min")

	def testTarifaHorariodif(self):
	# Calculo de tarifa trabajando con los dos tipos de tasas
		precios = Tarifa(1, 2)
		tiempoDeTrabajo = [datetime(2016, 4, 22, 23, 0, 0), datetime(2016, 4, 23, 0, 10, 0)]
		pago = calcularPrecio(precios,tiempoDeTrabajo)
		assert((pago==5.0, "se pagó correctamente")

	def testTaritfahorinterca(self):
	# Calculo de tarifa empezando en un tipo de tasa y terminando
	# en el mismo tipo de tasa pero teniendo en cuenta que 
	# completo  
		precios = Tarifa(1, 2)
		tiempoDeTrabajo = [datetime(2016, 4, 22, 23, 0, 0), datetime(2016, 4, 26, 0, 10, 0)]
		pago = calcularPrecio(precios,tiempoDeTrabajo)
		assert(pago==122.0, "se pagó correctamente")
