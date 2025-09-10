import calculadora as calc

# tipados dinámicos
resultado = 10
resultado = ("hola")


# a = input("dame un número") #lo que metamos siempre lo va a interpretar como un string
# a = a + 10 #no se puede, hay que castear
# a = float(input("dame un número")) #cambiamos la variable a float
# print(a)

# métodos
def miPrimerMetodo():
    nombre = "Francisco"
    print(nombre)
    apellido = "Alia"
    print(apellido)


miPrimerMetodo()  # solo se pueden llamar a los métodos después de crearlos
calc.sumar()

# condicionales
a = 20
b = 30

if a > 30:
    print("hola")
    if a > 100:
        print("que grande eres")
    elif a < 100:
        print("no eres tan grande")
else:
    print("adios")
