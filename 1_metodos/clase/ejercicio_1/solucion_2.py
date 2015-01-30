# -*- coding: utf-8 -*-
def mult_tres(n):
	n % 3 == 0

def mult_cinco(n):
	n % 5 == 0

def condicion(n):
	mult_tres(n) or mult_cinco(n)

def suma(n):
	i = 1
	suma = 0
	while i < n:
		if condicion(i):
			suma = suma + i
		i = i + 1
	print suma

suma(1000)