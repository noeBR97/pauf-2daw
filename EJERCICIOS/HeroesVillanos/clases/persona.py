from datetime import date
import uuid

class Persona:
    def __init__(self, nombre, apellidos, fecha_nacimiento, puntuacion_total):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__fecha_nacimiento = fecha_nacimiento
        self.__puntuacion_total = puntuacion_total
        self.__id = uuid.uuid4()


    def __str__(self):
        print("ID: " + str(self.__id) + "\n"
              "Nombre: " + str(self.__nombre) + "\n"
              "Apellidos: " + str(self.__apellidos) + "\n"
              "Fecha nacimiento: " + str(self.__fecha_nacimiento) + "\n"
              "Puntuación total: " + str(self.__puntuacion_total) + "\n")