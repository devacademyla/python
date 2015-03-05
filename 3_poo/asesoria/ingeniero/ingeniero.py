# -*- coding: utf-8 -*-

import random


class Dado(object):
    def __init__(self):
        self.lista = []

    @staticmethod
    def lanzar_dado():
        return random.randint(1, 6)

    def num_dados(self, n):
        for i in range(n):
            self.lista += [self.lanzar_dado()]
        return self.lista


class Ingeniero(Dado):

    def __init__(self, *args, **kwargs):
        super(Ingeniero, self).__init__(*args, **kwargs)
        self.n = 5
        self.list_numeros = self.num_dados(self.n)
        self.num_escogido = []
        self.preguntas = [u'Primer número: ', u'Sumar el numero: ',
                          u'Restar el número: ', u'Multiplicar el número: ',
                          u'Dividir el número: ']

    def escoger(self):
        print(self.list_numeros)
        for pregunta in self.preguntas:
            input_correcto = False
            while input_correcto is False:
                input_num = int(raw_input(pregunta))
                if input_num in self.list_numeros:
                    self.num_escogido.append(input_num)
                    self.list_numeros.remove(input_num)
                    input_correcto = True
                else:
                    input_correcto = False
                    print 'El número ingresado no se encuentra.'
        return self.num_escogido

    def resultado(self):
        dados = self.num_escogido
        resultado = dados[0] + dados[1]
        resultado -= dados[2]
        resultado *= float(dados[3])
        resultado /= float(dados[4])
        return resultado

if __name__ == '__main__':
    ingenieros = Ingeniero()
    print("Lista de números ingresados: {}".format(ingenieros.escoger()))
    print("El resultado es {:.2f}".format(ingenieros.resultado()))
