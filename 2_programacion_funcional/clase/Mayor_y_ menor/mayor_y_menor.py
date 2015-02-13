# -*- coding: utf-8 -*-
def comparar(*numeros):
	mayor, menor = 0, 1000
	for a in numeros:
		if a > mayor:
			mayor = a
	print "El número mayor es",mayor
	for b in numeros:		
		if b < menor:
			menor = b
	print "El número menor es",menor
	
comparar(2,5,6,7,12,234,4,6)
