# -*- coding: utf-8 -*-

import unittest
from xmen import Xmen, Magneto, ProfesorX


class XmenTest(unittest.TestCase):
    def setUp(self):
        self.xmen = Xmen(u"Wolverine").demostrar_poder()
        self.magneto_poder = Magneto(u"Magneto").demostrar_poder()
        self.profesorx_poder = ProfesorX(u"Profesor X").demostrar_poder()

    def test_xmen(self):
        assert self.xmen.endswith(
            u'estoy descubriendo mi poder')

    def test_magneto(self):
        assert self.magneto_poder.endswith(
            u'puedo controlar objetos metálicos')

    def test_profesorx(self):
        assert self.profesorx_poder.endswith(u'y tengo telepatía')

if __name__ == '__main__':
     unittest.main()
