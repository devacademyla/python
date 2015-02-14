# -*- coding: utf-8 -*-
import unittest
from tortuga import lanzar_dado, num_dados, resultado, calculo


class TestTortuga(unittest.TestCase):
    def setUp(self):
        self.lanzar = lanzar_dado()
        self.cubilete = num_dados(5)
        self.resultado_dado = resultado(True, False, 0)
        self.resultado_una_pata = resultado(True, True, 1)
        self.resultado_patas = resultado(True, True, 4)

    def test_dado(self):
        """el resultado es un número aleatorio entre 1 y 6"""
        self.assertLess(0, self.lanzar)     # 0 < ?
        self.assertGreaterEqual(6, self.lanzar)  # 6 >= ?

    def test_cubilete(self):
        """el cubilete tiene 5 dados"""
        self.numeros_dados = len(self.cubilete)
        self.assertEqual(5, self.numeros_dados)

    def test_caparazon(self):
        """Obteniendo de uno de los cinco dados un 6"""
        self.lanzada = calculo(False, False, 0, 5, [4, 5, 6, 4, 2])
        caparazon, patas, num_patas = self.lanzada[0:3]
        self.resultado_dado = resultado(caparazon, patas, num_patas)
        self.vale = self.assertMultiLineEqual("Tengo el caparazón", self.resultado_dado)

    def test_una_pata(self):
        """Obteniendo de uno de los cinco dados un 1"""
        self.lanzada = calculo(False, False, 0, 5, [4, 5, 6, 1, 2])
        caparazon, patas, num_patas = self.lanzada[0:3]
        self.resultado_una_pata = resultado(caparazon, patas, num_patas)
        self.assertMultiLineEqual("Tengo el caparazón \nTengo 1 pata", self.resultado_una_pata)

    def test_patas(self):
        """sacando la jugada perfecta"""
        self.lanzada = calculo(False, False, 0, 5, [1, 1, 6, 1, 1])
        caparazon, patas, num_patas = self.lanzada[0:3]
        self.resultado_patas = resultado(caparazon, patas, num_patas)
        self.assertMultiLineEqual("Tengo el caparazón \nTengo 4 patas", self.resultado_patas)

    def test_caculo(self):
        """evaluando la funcion calculo para saber si acumula y quita los dados
        deacuerdo al resultado """
        self.lanzada = calculo(False, False, 0, 5, [4, 5, 6, 1, 2])
        self.assertTupleEqual((True, True, 1, 3, [4, 5, 6, 1, 2]), self.lanzada)

    def test_resultados(self):
        """Obteniendo una pata"""
        self.lanzada = calculo(False, False, 0, 5, [4, 5, 6, 1, 2])
        caparazon, patas, num_patas = self.lanzada[0:3]
        self.resultado_dados = resultado(caparazon, patas, num_patas)
        self.assertMultiLineEqual("Tengo el caparazón \nTengo 1 pata", self.resultado_dados)

# python -m unittest -v tortugas2
