import unittest
from darth_vader import DarthVader, Luke


class Padre(unittest.TestCase):

    def setUp(self):
        self.padre = DarthVader()
        self.hijo = Luke()

    def test_profesion(self):
        self.assertEqual((self.padre.profesion(), self.hijo.profesion()), ('maestro jedi', 'maestro jedi'))

    def test_padre(self):
        self.assertEqual(self.padre.hablar(), 'Luke, yo soy tu padre')

    def test_hijo(self):
        self.assertEqual(self.hijo.hablar(), 'Noooooooooooooooo!!!')

# python -m unittest -v darth_vader_test
