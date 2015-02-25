import unittest
from darth_vader import DarthVader, Luke


class Padre(unittest.TestCase):

    def setUp(self):
        self.padre = DarthVader(u"Darth Vader")
        self.hijo = Luke(u"Luke Skywalker")

    def test_profesion(self):
        self.assertEqual(
            (self.padre.profesion(), 
            self.hijo.profesion()),
            (u'Maestro Jedi', 'Maestro Jedi'))

    def test_padre(self):
        self.assertEqual(self.padre.hablar(),
            u'Darth Vader: Luke, yo soy tu padre')

    def test_hijo(self):
        self.assertEqual(self.hijo.hablar(),
            u'Luke Skywalker: Noooooooooooooooo!!!')

if __name__ == '__main__':
    unittest.main()
