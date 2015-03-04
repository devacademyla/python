# -*- coding: utf-8 -*-

import unittest
from ingeniero import Dado, Ingeniero
import mock


class IngenieroTest(unittest.TestCase):

    def setUp(self):
        self.dado = Dado()
        self.inge = Ingeniero()

    def test_dado(self):
        """El resultado del dado es un número aleatorio entre 1 y 6"""
        resultado = Dado.lanzar_dado()
        self.assertLess(0, resultado)     # 0 < ?
        self.assertGreaterEqual(6, resultado)  # 6 >= ?

    def test_num_dados(self):
        """El cubilete debe tener solo 5 dados"""
        self.numeros_dados = len(self.dado.num_dados(5))
        self.assertEqual(5, self.numeros_dados)

    def test_ingeniero_resultado(self):
        """Ingresando la list [5,4,3,2,1] debe retornar 12
        :return: 12
        """
        self.inge.num_escogido = [5, 4, 3, 2, 1]
        self.assertEqual(self.inge.resultado(), 12)

if __name__ == '__main__':
    unittest.main()