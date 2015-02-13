# -*- coding: utf-8 -*-
def suma(a, b):
    return int(a) + int(b)

resultado = 2 ** 100
lista_de_numeros = list(str(resultado))

print reduce(suma, lista_de_numeros)
