import unittest
from persona_saluda import Persona


class PersonaUnitTest(unittest.TestCase):

    def setUp(self):
        self.persona = Persona('pedro')
        self.nombre = self.persona.mi_nombre()
        self.te_saludo = self.persona.saludar()

    def test_nombre(self):
        self.assertEqual(self.nombre, 'pedro')

    def test_saludando(self):
        self.assertEqual(self.te_saludo, 'Hola, mi nombre es pedro')
