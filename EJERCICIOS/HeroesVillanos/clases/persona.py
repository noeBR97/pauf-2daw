from datetime import date

class Persona:
    def __init__(self, nombre, apellidos, anio, mes, dia, id):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__anio = anio
        self.__mes = mes
        self.__dia = dia
        self.__edad = self.calcularEdad()
        self.__id = id


    def calcularEdad(self):
        fecha_nacimiento = date (self.__anio, self.__mes, self.__dia)
        dia_actual = date.today()
        edad = dia_actual.year - fecha_nacimiento.year
        return edad