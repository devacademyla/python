# -*- coding: utf-8 -*-
import random


class Dado(object):

    @staticmethod
    def lanzar_dado():
        return random.randint(1, 6)


class Todito(Dado):

    def __init__(self, *args, **kwargs):
        super(Todito, self).__init__(*args, **kwargs)
        self.dado = self.lanzar_dado()
        self.definir_castigo()

    def definir_castigo(self):
        if self.dado in (1, 5):
            return "Toman todos"
        if self.dado in (2, 6):
            return "Toma otro"
        if self.dado is 3:
            return "Toma el de la derecha"
        if self.dado is 4:
            return "Toma el de la izquierda"

    def jugar(self):
        return self.dado


class Jugador(object):

    def __init__(self, id_user):
        self.id = id_user
        self.shots = 0

    def tomar(self):
        self.shots += 1
        return self.shots

    def esta_borracho(self):
        if self.shots == 10:
            return "esta ebrio"
        else:
            return False


class Juego(object):
    def __init__(self, num_jugadores):
        self.todito = Todito()
        self.jugadores = []
        for i in range(0, num_jugadores):
            self.jugadores.append(Jugador(i))

    def aplicar_castigo(self, castigo, jugador, count):

        if castigo == "Toman todos":
            for i in self.jugadores:
                i.tomar()
        elif castigo == "Toma otro":
            jugador_elegido = random.choice(self.jugadores)
            jugador_elegido.tomar()

        elif castigo == "Toma el de la derecha":
            if jugador == self.jugadores[-1].id:
                self.jugadores[0].tomar()
            else:
                self.jugadores[count + 1].tomar()
        elif castigo == "Toma el de la izquierda":
            if jugador == self.jugadores[0].id:
                self.jugadores[-1].tomar()
            else:
                self.jugadores[count - 1].tomar()
        else:
            return None

    def quitar_jugador(self):
        """ Elimina al jugador que tiene 10 shots """
        i = len(self.jugadores)-1
        while i >= 0:
            if self.jugadores[i].esta_borracho():
                del(self.jugadores[i])
            if len(self.jugadores) == 1:
                break
            i -= 1

    def jugar(self):
        """ Al ultimo jugador en tener 10 shots
        :return: jugador ganador
        """
        while True:
            count = 0
            for i in self.jugadores:
                if i:
                    self.aplicar_castigo(self.todito.definir_castigo(), i.id, count)
                    count += 1
                    self.quitar_jugador()
                if len(self.jugadores) == 1:
                    break
            if len(self.jugadores) == 1:
                    break

        return self.jugadores[0].id

if __name__ == '__main__':
    todito = Todito()
    juego = Juego(5)
    print juego.jugar(), 'jugador ganador'
