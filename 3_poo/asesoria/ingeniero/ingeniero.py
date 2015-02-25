# -*- coding: utf-8 -*-
import random
 
class Dado:
	def lanzar_dado(self):
		return 1 + random.randrange(6)
 
	def num_dados(self, n):
		self.lista = []
		for i in range(n):
			self.lista += [self.lanzar_dado()]
 		print self.lista
		return self.lista
 
 
class Ingeniero(Dado):
	def escoger(self):
		self.preguntas = ['Primer número: ', 'Sumar el número: ',
						'Restar el número: ', 'Multiplicar el número: ',
						'Dividir el número: ']
		return self.preguntas
 
	def resultado(self):
		n = 5
		dados = self.num_dados(n)
		pregunta = self.escoger()
 		for i in range(0, n):
			print pregunta[i], dados[i]
 		resultado = dados[0] + dados[1]
		resultado -= dados[2]
		resultado *= float(dados[3])
		resultado /= float(dados[4])
		print "Obtuviste", resultado
 
	def __init__(self):
		""" La funcion magica __init__ se ejecuta al llama la clase Ingeniero ,
		ejecutandose la funcion resultado """
		self.resultado()
 
ingeniero = Ingeniero()
ingeniero