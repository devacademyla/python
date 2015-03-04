# -*- coding: utf-8 -*-
import unittest
from todito import *


class ToditoUnittest(unittest.TestCase):

    def setUp(self):
        self.dado = Dado()
        self.todito = Todito()
        self.jugador = Jugador(1)

    def test_dado(self):
        """test_dado El resultado del dado es un numero aleatorio entre 1 y 6"""
        self.resultado = self.dado.lanzar_dado()
        self.assertLess(0, self.resultado)     # 0 < ?
        self.assertGreaterEqual(6, self.resultado)  # 6 >= ?

    def test_dado_resultado(self):
        """test_dado_resultado retornar el numero de dado otenido"""
        dado = self.todito.jugar()
        self.assertLess(0, dado)     # 0 < ?
        self.assertGreaterEqual(6, dado)  # 6 >= ?

    def test_definir_castigo(self):
        """test_definir_castigo al obtener 4 como resultado deberia retornar el castigo 'Toma el de la izquierda'"""
        self.todito.dado = 4
        castigo = self.todito.definir_castigo()
        self.assertEqual(castigo,  "Toma el de la izquierda", 'No se obtuvo el castigo esperado')

    def test_shot(self):
        """test_jugador_shot los shot deben iniciar en 0"""
        self.assertEqual(0, self.jugador.shots)

    def test_toma_shot(self):
        """test_jugador_toma_shot debe iniciar een cero"""
        self.jugador.shots = 0
        self.toma = self.jugador.tomar()
        self.assertEqual(self.toma, 1)

    def test_jugador(self):
        """test_jugador al tener 10 shot debe retornar 'esta ebrio'"""
        self.jugador.shots = 10
        self.borracho = self.jugador.esta_borracho()
        self.assertEqual(self.borracho, 'esta ebrio')

    def test_juego(self):
        """test_juego Ver si se agrego la cantidad de jugadores"""
        self.juego = Juego(3)
        numero = len(self.juego.jugadores)
        self.assertEqual(numero, 3)


if __name__ == '__main__':
    unittest.main()