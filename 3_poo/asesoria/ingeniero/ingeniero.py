# -*- coding: utf-8 -*-

import random
 
class Dado(object):

    def lanzar_dado(self):
        return 1 + random.randrange(6)
 
    def num_dados(self, n):
        self.lista = []
        for i in range(n):
            self.lista += [self.lanzar_dado()]
        print self.lista
        return self.lista
 
 
class Ingeniero(Dado):

    def __init__(self, *args, **kwargs):
        """ La funcion magica __init__ se ejecuta al llama la
        clase Ingeniero, ejecutándose la funcion resultado """
        super(Ingeniero, self).__init__(*args, **kwargs)
        self.resultado()


    def escoger(self):
        self.preguntas = [
            u'Primer número: ', u'Sumar el número: ',
            u'Restar el número: ', u'Multiplicar el número: ',
            u'Dividir el número: ']
        return self.preguntas
 

    def resultado(self):
        n = 5
        dados = self.num_dados(n)
        pregunta = self.escoger()
        for i in range(0, n):
            print pregunta[i], dados[i]
        resultado = dados[0] + dados[1]
        resultado -= dados[2]
        resultado *= float(dados[3])
        resultado /= float(dados[4])
        print u"Obtuviste", resultado
 

if __name__ == '__main__':
    ingeniero = Ingeniero()
