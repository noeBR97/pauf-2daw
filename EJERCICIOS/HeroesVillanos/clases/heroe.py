import random

from persona import Persona

class Heroe(Persona):
    def __init__(self, nombre, apellidos, fecha_nacimiento):
        self.__codigo_limpio = random.randint(0, 100)
        self.__bien_documentado = random.randint(0, 100)
        self.__git_god = random.randint(0, 100)
        self.__arquitecto = random.randint(0, 100)
        self.__detallista = random.randint(0, 100)
        puntuacion_total = self.puntuacion_total_heroe(self.__codigo_limpio, self.__bien_documentado, self.__git_god, self.__arquitecto, self.__detallista)
        super(Persona, self).__init__(nombre, apellidos, fecha_nacimiento, puntuacion_total)



    def puntuacion_total_heroe(codigo_limpio, bien_documentado, git_god, arquitecto, detallista):
        suma_poderes = sum([codigo_limpio, bien_documentado, git_god, arquitecto, detallista])
        puntuacion_total = (suma_poderes * 100) / 500
        return int(puntuacion_total)


