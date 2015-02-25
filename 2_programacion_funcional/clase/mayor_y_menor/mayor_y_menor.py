#!/usr/bin/env pythoh
# -*- coding: utf-8 -*-

def comparar(*numeros):
	mayor, menor = 0, 1000
	for a in numeros:
		if a > mayor:
			mayor = a
	print u"El número mayor es", mayor
	for b in numeros:		
		if b < menor:
			menor = b
	print u"El número menor es", menor

if __name__ == '__main__':
    comparar(2,5,6,7,12,234,4,6)
