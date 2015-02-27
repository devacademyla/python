# -*- coding: utf-8 -*-

import random


class Dado(object):

    def lanzar_dado(self):
        return 1 + random.randrange(6)

    def num_dados(self, n):
        self.lista = []
        for i in range(n):
            self.lista += [self.lanzar_dado()]
        return self.lista


class Ingeniero(Dado):

    def __init__(self, *args, **kwargs):
        """ La funcion magica __init__ se ejecuta al llama la
        clase Ingeniero, ejecutándose la funcion resultado """
        super(Ingeniero, self).__init__(*args, **kwargs)
        self.n = 5
        self.list_numeros = self.num_dados(self.n)
        self.num_escogido = []
        self.escoger()
        self.resultado()

    def escoger(self):
        print self.list_numeros

        preguntas = [
            u'Primer numero: ', u'Sumar el numero: ',
            u'Restar el numero: ', u'Multiplicar el numero: ',
            u'Dividir el numero: ']

        for pregunta in preguntas:
            num = False
            while num is False:
                num = int(raw_input(pregunta))
                if num in self.list_numeros:
                    self.list_numeros.remove(num)
                    self.num_escogido.append(num)
                else:
                    num = False
                    print 'El número ingresado no se encuentra.'

        return self.num_escogido

    def resultado(self):
        dados = self.num_escogido
        resultado = dados[0] + dados[1]
        resultado -= dados[2]
        resultado *= float(dados[3])
        resultado /= float(dados[4])
        print u"Obtuviste", resultado


if __name__ == '__main__':
    ingeniero = Ingeniero()
