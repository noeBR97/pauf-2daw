import logging
from datetime import datetime

class Log:
    fecha = datetime.now().strftime("%d%m%Y").lower()
    nombre_fichero = f"log/{fecha}_HEROESYVILLANOS.log"