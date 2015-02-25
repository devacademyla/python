import unittest
from persona_saluda import Persona


class PersonaUnitTest(unittest.TestCase):

    def setUp(self):
        self.persona = Persona(u'Pedro')
        self.nombre = self.persona.mi_nombre()
        self.te_saludo = self.persona.saludar()

    def test_nombre(self):
        self.assertEqual(self.nombre, u'Pedro')

    def test_saludando(self):
        self.assertEqual(self.te_saludo, u'Hola, mi nombre es Pedro')


if __name__ == '__main__':
    unittest.main()
