# -*- coding: utf-8 -*-

import random

def lanzar_dado():
    return 1 + random.randrange(6)

def definir_castigo(dado):
    if dado == 1 or dado == 5:
        print "Toman todos"
    if dado == 2 or dado == 6:
        print "Toma otro"
    if dado == 3:
        print "Toma el de la derecha"
    if dado == 4:
        print "Toma el de la izquierda"

def jugar():
    dado = lanzar_dado()
    print u"Salió el valor", dado, u"entonces:"
    castigo = definir_castigo(dado)

if __name__ == '__main__':
    jugar()
