import random

from persona import Persona

class Villano(Persona):
    def __init__(self, nombre, apellidos, fecha_nacimiento):
        super(Persona, self).__init__(nombre, apellidos, fecha_nacimiento)
        self.__chagepeteador = random.randint(0, 100)
        self.__entregador_tardio = random.randint(0, 100)
        self.__ausencias = random.randint(0, 100)
        self.__hablador = random.randint(0, 100)
        puntuacion_total = self.puntuacion_total_villano(self.__chagepeteador, self.__entregador_tardio, self.__ausencias, self.__hablador)
        super(Persona, self).__init__(nombre, apellidos, fecha_nacimiento, puntuacion_total)

    def puntuacion_total_villano(chagepeteador, entregador_tardio, ausencias, hablador):
        suma_poderes = sum([chagepeteador, entregador_tardio, ausencias, hablador])
        puntuacion_total = (suma_poderes * 100) / 400
        return int(puntuacion_total)
