# -*- coding: utf-8 -*-


class Xmen:

    def demostrar_poder(self):
        return 'Descubriendo poder'


class Magneto(Xmen):

    def demostrar_poder(self):
        return 'Controlar objetos metalicos'


class ProfesorX(Xmen):

    def demostrar_poder(self):
        return 'Telepatía'
print Magneto().demostrar_poder()
