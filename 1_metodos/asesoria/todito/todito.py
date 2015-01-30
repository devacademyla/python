# -*- coding: utf-8 -*-
import random

def lanzar_dado():
	dado = 1 + random.randrange(6)
	print "Dado" , dado , "y el castigo es: "
	if dado == 1 or dado == 5:
		print "Toman todos"
	if dado == 2 or dado == 6:
		print "Toma otro"
	if dado == 3:
		print "Toma el de la derecha"
	if dado == 4:
		print "Toma el de la izquierda"

lanzar_dado()