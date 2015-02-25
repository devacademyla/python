#!/usr/bin/env python

suma_de_cuadrados = 0

cuadrado_de_suma = 0

suma = 0

for i in range(100 + 1):
    cuadrado = i ** 2
    suma_de_cuadrados += cuadrado
    suma += i

cuadrado_de_suma = suma ** 2

print "Cuadrado de suma: %d" % cuadrado_de_suma
