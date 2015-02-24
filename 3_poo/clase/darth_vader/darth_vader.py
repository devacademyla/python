class Especialidad:
    def profesion(self):
        return 'maestro jedi'


class DarthVader(Especialidad):
    def hablar(self):
        return 'Luke, yo soy tu padre'


class Luke(Especialidad, DarthVader):
    """Luke hereda los metodos de DarthVader"""
    def hablar(self):
        return 'Noooooooooooooooo!!!'
