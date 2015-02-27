# -*- coding: utf-8 -*-

import random

class Dado(object):

    def lanzar_dado(self):
        return 1 + random.randrange(6)

class Todito(Dado):

    def __init__(self, *args, **kwargs):
        """ La funcion magica __init__ se ejecuta al llama la
        clase Ingeniero, ejecutándose la funcion resultado """
        super(Todito, self).__init__(*args, **kwargs)
        self.dado = self.lanzar_dado()
        self.jugar()
        self.definir_castigo() 
        

    def definir_castigo(self):
        if self.dado == 1 or self.dado == 5:
            print "Toman todos"
        if self.dado == 2 or self.dado == 6:
            print "Toma otro"
        if self.dado == 3:
            print "Toma el de la derecha"
        if self.dado == 4:
            print "Toma el de la izquierda"

    def jugar(self):
        print u"Salió el valor", self.dado, u"entonces:"

if __name__ == '__main__':
    todito = Todito()
