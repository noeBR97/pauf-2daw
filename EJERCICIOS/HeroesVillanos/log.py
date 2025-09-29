import logging
from datetime import datetime
import os

class Log:
    def __init__(self):
        fecha = datetime.now().strftime("%d%m%Y").lower()
        nombre_fichero = f"log/{fecha}_HEROESYVILLANOS.log"

        output_dir = './logs'
        if not os.path.isdir(output_dir):
            os.mkdir(output_dir)

        logger = logging.getLogger('heroes_y_villanos_log')
        logging.basicConfig(filename=output_dir + "/" + nombre_fichero, encoding='utf-8', level=logging.DEBUG)
        logging.basicConfig(format='%(asctime)s %(message)s')
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)