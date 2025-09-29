import random

from persona import Persona

class Heroe:
    def __init__(self, nombre, apellidos, fecha_nacimiento, id):
        super(Persona, self).__init__(nombre, apellidos, fecha_nacimiento, id)
        self.__codigo_limpio = random.randint(0, 100)
        self.__bien_documentado = random.randint(0, 100)
        self.__git_god = random.randint(0, 100)
        self.__arquitecto = random.randint(0, 100)
        self.__detallista = random.randint(0, 100)


    