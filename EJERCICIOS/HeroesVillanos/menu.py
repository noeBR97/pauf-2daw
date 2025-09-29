import logging
import os
from datetime import datetime


fecha = datetime.now().strftime("%d%m%Y").lower()
nombre_fichero = f"{fecha}_HEROESYVILLANOS.log"

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






def menu(logger):
    fin = False
    while not fin:
        opcion = ""
        opcion_correcta = False

        print("1- Listar Héroes\n"
              "2- Listar Villanos\n"
              "3- Crear héroe\n"
              "4- Crear villano\n"
              "5- Realizar búsqueda\n"
              "6- Emparejar héroe y villano\n"
              "7- SALIR")

        while not opcion_correcta:
            opcion = int(input("Elige una opción: "))
            if opcion in [1, 2, 3, 4, 5, 6, 7]:
                opcion_correcta = True
            else:
                logger.warning("Elige una opción correcta.")

        if opcion == 1:
            logger.debug("El usuario ha elegido la opción 1.")
            ""
            #listamos héroes
        elif opcion == 2:
            ""
            #listamos villanos
        elif opcion == 3:
            ""
            #creamos héroe
        elif opcion == 4:
            ""
            #creamos villano
        elif opcion == 5:
            ""
            #buscamos por atributo
        elif opcion == 6:
            ""
            #emparejamos
        elif opcion == 7:
            fin = True
        else:
            print("Opción no permitida.")

def main():
    try:
        logger.info("Iniciando ejecución")
        menu(logger)
    except Exception as e:
        print(f"TODOS LOS ERRORES AL LOG {e}")


if __name__ == "__main__":
    main()