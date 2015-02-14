# -*- coding: utf-8 -*-
import random

def lanzar_dado():
<<<<<<< HEAD
    return 1 + random.randrange(6)

def num_dados(n):
    lista = []
    for i in range(n):
        lista += [lanzar_dado()]
    return lista

def resultado(caparazon, patas, num_patas):
    # print caparazon, patas, num_patas
    if caparazon is True:
        if patas is True:
            if num_patas < 2:
                return "Tengo el caparazón \nTengo {} pata".format(num_patas)
            elif num_patas >= 2:
                return "Tengo el caparazón \nTengo {} patas".format(num_patas)
        else:
            return "Tengo el caparazón"
    else:
        return "No tengo nada"


def calculo(caparazon, patas, num_patas, n, dados):

    dados = dados
    # print dados
    if caparazon:
        if 1 in dados:
            patas = True
            for i in dados:
                if i == 1:
                    num_patas += 1
                    n -= 1
    elif 6 in dados:
        caparazon = True
        n -= 1
        if 1 in dados:
            patas = True
            for i in dados:
                if i == 1:
                    num_patas += 1
                    n -= 1

    return caparazon, patas, num_patas, n, dados


def juego():
    caparazon = False
    patas = False
    num_patas = 0
    n = 5
    jugadas = 3
    while jugadas > 0:
        dados = num_dados(n)
        caparazon, patas, num_patas, n, dados = calculo(caparazon, patas, num_patas, n, dados)
        print dados
        print resultado(caparazon, patas, num_patas)
        jugadas -= 1
juego()
=======
	return 1 + random.randrange(6)

def num_dados(n):
	lista = []
	for i in range(n):
		lista += [lanzar_dado()]
	return lista

def juego():
	caparazon = False
	patas = False
	num_patas = 0
	jugadas = 3
	n = 5
	while jugadas > 0:
		dados = num_dados(n)
		print dados
		if caparazon:
			if 1 in dados:
				patas = True
				for i in dados:
					if i == 1:
						num_patas += 1
						n -= 1
		elif 6 in dados:
			caparazon = True
			n -= 1
			if 1 in dados:
				patas = True
				for i in dados:
					if i == 1:
						num_patas += 1
						n -= 1
		if caparazon == True:
			print "Tengo el caparazón"
			if patas == True:
				if num_patas < 2:
					print "Tengo", num_patas, "pata"
				elif num_patas >= 2:
					print "Tengo", num_patas, "patas"
		else:
			print "No tengo nada"
		jugadas -= 1

juego()
>>>>>>> 148d32431812a1a791c73774bae5f32e33caa3a9
