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

class tareaTester(unittest.TestCase):

							#################################
							##       Pruebas unitarias     ##
							#################################

	def testTasaIgual(self):
	# tasas Distintas						
	def testMinMInutos(self):
	# Minimo de minutos que debe trabajar una persona para facturar
	def testMaxDias(self):
	# Prueba que verifica el maximo de dias que puede trabajar  una persona
	def testFakeDateString(self, DD, MM, AA, horas, minutos, segundos, DD2, MM2, AA2, horas2, minutos2, segundos2):
	# Prueba que verifica el tipo de datos de las fechas
	def testFakeDataNegative(self, DD, MM, AA, horas, minutos, segundos, DD2, MM2, AA2, horas2, minutos2, segundos2):
	# Prueba que verifica el tipo de datos de las fechas

							###########################################
							##          Pruebas de aceptacion        ##
							###########################################

	
	def testHoraSalidamasTemprano(self, horas, minutos, segundos, horas2, minutos2, segundos2):
	# Prueba que verifica el orden de las horas
	def testHorasiguales(self, DD, MM, AA, horas, minutos, segundos, DD2, MM2, AA2, horas2, minutos2, segundos2):
	# Horas distintas
	def testTarifaHorariodif(self, DD, MM, AA, horas, minutos, segundos, DD2, MM2, AA2, horas2, minutos2, segundos2):
	# Calculo de tarifa trabajando con los dos tipos de tasas
	def testTaritfahorinterca(self, DD, MM, AA, horas, minutos, segundos, DD2, MM2, AA2, horas2, minutos2, segundos2):
	# Calculo de tarifa empezando en un tipo de tasa y terminando
	# en el mismo tipo de tasa pero teniendo en cuenta que 
	# completo  