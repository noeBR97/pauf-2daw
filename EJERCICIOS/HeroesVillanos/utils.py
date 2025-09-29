import json

from clases.heroe import Heroe
from clases.villano import Villano


def crear_personaje():
    pj = None
    is_heroe_bl = False
    aux_is_heroe_str = ""

    # BUCLE PARA OBTENER POR TECLADO. SE REPITE HASTA QUE SE INTRDUZCAN VALORES ACEPTADOS
    while aux_is_heroe_str not in ["SI", "S", "NO", "N"]:
        aux_is_heroe_str = input("¿Quieres crear un heroe? Introduce si/no")
        if aux_is_heroe_str.lower() in (["SI", "S", ]):
            is_heroe_bl = True

            # SE LLAMA A UNA FUCNIÓN PARA OBTENER VALORES POR TECLADO
    nombre_str, apellidos_str, fecha_str = obtener_atributos_comunes_desde_teclado()

    # SE COMPRUEBA SI SE DESEA CREAR HEROE O VILLANO Y SE ASIGNA A LA VARIABLE A DEVOLVER
    if is_heroe_bl:
        pj = Heroe(nombre_str, apellidos_str, fecha_str)
    else:
        pj = Villano(nombre_str, apellidos_str, fecha_str)

    # ESTA LINEA ES IGUAL QUE EL IF ELSE DE ARRIBA. ES OTRA FORMA DE ASIGNAR UN VALOR
    # pj = Heroe(nombre_str, apellidos_str, fecha_str) if is_heroe_bl == True else Villano(nombre_str, apellidos_str, fecha_str)

    return pj


def obtener_atributos_comunes_desde_teclado():
    nombre_str = ""
    apellidos_str = ""
    fecha_str = ""

    while nombre_str == "":
        nombre_str = input("Introduce el nombre: ")

    while apellidos_str == "":
        apellidos_str = input("Introduce los apellidos: ")

    # ESTO STRING SE PODRÍA SUSTITUIR POR UN OBJETO DE LA CLASE DATE (LIBRERIA PROPIA DE PYTHON)
    while fecha_str == "":
        fecha_str = input("Introduce la fecha de nacimiento: ")

    return nombre_str, apellidos_str, fecha_str

def registrar_heroe_en_json():
    nuevos_datos_python = []

    with open("./archivos_json/heroes.json", 'r') as archivo:
        datos_python = json.load(archivo)

    pj = crear_personaje()

    es_mi_clase = isinstance(pj, Heroe)

    nuevos_datos_python = pj.to_list()

    # Escribir el archivo JSON actualizado
    with open("./archivos_json/personajes/heroes.json", 'w') as archivo:
        json.dump(nuevos_datos_python, archivo, indent=4)

def registrar_villano_en_json():
    nuevos_datos_python = []

    with open("./archivos_json/villanos.json", 'r') as archivo:
        datos_python = json.load(archivo)

    pj = crear_personaje()

    es_mi_clase = isinstance(pj, Villano)

    nuevos_datos_python = pj.to_list()

    # Escribir el archivo JSON actualizado
    with open("./archivos_json/villanos.json", 'w') as archivo:
        json.dump(nuevos_datos_python, archivo, indent=4)

def listar_heroes():
    ruta = "./archivos_json/heroes.json"

    with open(ruta, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        print(f"HEROES:\n{datos}\n")

def listar_villanos():
    ruta = "./archivos_json/villanos.json"

    with open(ruta, 'r', encoding='utf-8') as f:
        datos = json.load(f)
        print(f"VILLANOS:\n{datos}\n")