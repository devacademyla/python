# -*- coding: utf-8 -*-


class Especialidad(object):

    def profesion(self):
        return u'Maestro Jedi'


class DarthVader(Especialidad):

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return u'%s: Luke, yo soy tu padre' % self.nombre


class Luke(DarthVader):
    """Luke hereda los metodos de DarthVader"""

    def hablar(self):
        return u'%s: Noooooooooooooooo!!!' % self.nombre


if __name__ == '__main__':
    print "Hace mucho tiempo en una lejana galaxia..."
    darth_vader = DarthVader("Darth Vader")
    luke = Luke("Luke Skywalker")
    print darth_vader.hablar()
    print luke.hablar()
