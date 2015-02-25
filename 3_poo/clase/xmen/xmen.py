# -*- coding: utf-8 -*-


class Xmen(object):

    def __init__(self, nombre):
        self.nombre = nombre

    def demostrar_poder(self):
        return u'Soy %s y estoy descubriendo mi poder' % self.nombre


class Magneto(Xmen):

    def demostrar_poder(self):
        return u'Soy %s y puedo controlar objetos metálicos' % self.nombre


class ProfesorX(Xmen):

    def demostrar_poder(self):
        return u'Soy %s y tengo telepatía' % self.nombre

if __name__ == '__main__':
    objetos = [Magneto("Magneto"), ProfesorX("Profesor X")]
    for obj in objetos:
        print obj.demostrar_poder()
