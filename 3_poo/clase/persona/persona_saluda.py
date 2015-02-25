# -*- coding: utf-8 -*-

class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def mi_nombre(self):
        return self.nombre

    def saludar(self):
        return u"Hola, mi nombre es {}".format(self.nombre)

if __name__ == '__main__':
    persona = Persona('Pedro')
    print persona.mi_nombre()
    print persona.saludar()
