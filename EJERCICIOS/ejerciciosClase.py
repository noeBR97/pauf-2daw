#EJ-1
listaEquipos = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]

print(listaEquipos[0]," y ",listaEquipos[-1])
listaEquipos.append("Betis")
listaEquipos.insert(0, "Getafe")
listaEquipos.remove("Barcelona")

#EJ-2
locales = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]
visitantes = ["Athletic", "Betis", "Cádiz", "Villarreal", "Osasuna"]

partidos = [locales[0]+" vs "+visitantes[0], locales[1]+" vs "+visitantes[1], locales[2]+" vs "+visitantes[2], locales[3]+" vs "+visitantes[3], locales[4]+" vs "+visitantes[4]]
print(partidos)

partidos.remove(locales[3]+" vs "+visitantes[3])
print(partidos)

partidos.append("Espanyol vs Rayo Vallecano")
print(partidos)

#EJ-3
