# -*- coding: utf-8 -*-

import unittest
from xmen import Xmen, Magneto, ProfesorX


class XmenTest(unittest.TestCase):
    def setUp(self):
        self.xmen = Xmen().demostrar_poder()
        self.magneto_poder = Magneto().demostrar_poder()
        self.profesorx_poder = ProfesorX().demostrar_poder()

    def test_xmen(self):
        self.assertEqual(self.xmen, 'Descubriendo poder')

    def test_magneto(self):
        self.assertEqual(self.magneto_poder, 'Controlar objetos metalicos')

    def test_profesorx(self):
        self.assertEqual(self.profesorx_poder, 'Telepatia')
