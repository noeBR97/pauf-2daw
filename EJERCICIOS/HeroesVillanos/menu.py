def menu():
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
            opcion = input("Elige una opción: ")
            if opcion in [1, 2, 3, 4, 5, 6, 7]:
                opcion_correcta = True
            else:
                print("Elige una opción correcta.")

        if opcion == 1:
            #listamos héroes
        elif opcion == 2:
            #listamos villanos
        elif opcion == 3:
            #creamos héroe
        elif opcion == 4:
            #creamos villano
        elif opcion == 5:
            #buscamos por atributo
        elif opcion == 6:
            #emparejamos
        elif opcion == 7:
            fin = True
        else:
            print("Opción no permitida.")


def gestionAulaDeHeroesYVillanos(opcion):
    pass
def main():
    try:
        while True:
            menu()
            opcion = int(input("Que eliges"))
            if opcion >= 5:
                print("Selecciona una opcion valida")
            else:
                gestionAulaDeHeroesYVillanos(opcion)


    except Exception as e:
        print(f"TODOS LOS ERRORES AL LOG {e}")


if __name__ == "__main__":
    main()