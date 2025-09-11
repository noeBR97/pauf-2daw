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

#operadores logicos
#if x > 10 and x < 100:

#bucles
contador = 0
ciclos = ["DAM", "DAW", "ASIR"]
for ciclo in ciclos:
    print(ciclo)

for i in range(5, 20):
    print(i)

while contador > 20:
    print(contador)
    contador += 1

lista = ['Marta', 'Víctor', 'Cris', 'Noelia']
lista.append('Javi')
lista.remove('Javi')

alumno = lista.pop()#elimina y devuelve el último elemento
del lista[1]#eliminamos por clave
print(alumno)
print(lista)
lista.insert(2, 'Diego')#insertar en una posición concreta
print(lista)
del lista[:2]#elimina elementos desde la posicion 0 hasta la 2
lista.sort()#ordena alfabéticamente o de menor a mayor
lista.sort(reverse=True)#ordena al revés