import random

from persona import Persona

class Villano:
    def __init__(self, nombre, apellidos, fecha_nacimiento, id):
        super(Persona, self).__init__(nombre, apellidos, fecha_nacimiento, id)
        self.__chagepeteador = random.randint(0, 100)
        self.__entregador_tardio = random.randint(0, 100)
        self.__ausencias = random.randint(0, 100)
        self.__hablador = random.randint(0, 100)


