class Persona():
    def __init__(self, nombre):
        self.nombre = nombre

    def mi_nombre(self):
        return self.nombre

    def saludar(self):
        return "Hola, mi nombre es {}".format(self.nombre)

#saluda = Persona('pedro')
#print saluda.mi_nombre()
#print saluda.saludar()
