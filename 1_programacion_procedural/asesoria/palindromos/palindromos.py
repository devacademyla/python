# -*- coding: utf-8 -*-
cadena = raw_input("Introduce la cadena: ")
cont = 0
cadena2 = ""
es = True
 
for i in cadena:
    if i.isupper():
        i = i.lower()
    if i != " ":
        cadena2 = cadena2 + i
        cont = cont + 1
 
for i in range(cont/2):
    if cadena2[i] != cadena2[cont-i-1]:
        es = False
        break
 
if es == True:
    print "Es palíndromo"
else:
    print "No es palíndromo"
