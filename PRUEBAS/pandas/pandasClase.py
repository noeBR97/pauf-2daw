import pandas as pd

data = {
    'Nombre': ['Ana', 'Luis', 'Juan'],
    'Edad': [17, 22, 21],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla'],
    'Ciclo': ['DAW2', 'DAW1', 'DAM1'],
    'Mayor': [False, True, True]
}

datos = [
    {"ID": 1, "Nombre": "Ana",    "Edad": 20, "Curso": "DAW2", "Grupo": "A", "Ciudad": "Puertollano", "Nota": 7.5, "Becado": True,  "Creditos": 60, "FechaMatricula": "2024-09-10"},
    {"ID": 2, "Nombre": "Luis",   "Edad": 35, "Curso": "DAW2", "Grupo": "B", "Ciudad": "Ciudad Real", "Nota": 4.0, "Becado": False, "Creditos": 55, "FechaMatricula": "2024-09-12"},
    {"ID": 3, "Nombre": "María",  "Edad": 60, "Curso": "DAW1", "Grupo": "A", "Ciudad": "Toledo",       "Nota": 9.2, "Becado": True,  "Creditos": 65, "FechaMatricula": "2024-09-09"},
    {"ID": 4, "Nombre": "Pedro",  "Edad": 15, "Curso": "DAW1", "Grupo": "C", "Ciudad": "Albacete",     "Nota": 5.5, "Becado": False, "Creditos": 58, "FechaMatricula": "2024-09-15"},
    {"ID": 5, "Nombre": "Lucía",  "Edad": 22, "Curso": "DAW2", "Grupo": "A", "Ciudad": "Puertollano", "Nota": 8.8, "Becado": False, "Creditos": 61, "FechaMatricula": "2024-09-11"},
    {"ID": 6, "Nombre": "Diego",  "Edad": 44, "Curso": "DAW1", "Grupo": "B", "Ciudad": "Toledo",       "Nota": 6.2, "Becado": True,  "Creditos": 59, "FechaMatricula": "2024-09-13"},
    {"ID": 7, "Nombre": "Elena",  "Edad": 28, "Curso": "DAW2", "Grupo": "C", "Ciudad": "Ciudad Real", "Nota": 3.2, "Becado": False, "Creditos": 40, "FechaMatricula": "2024-09-10"},
    {"ID": 8, "Nombre": "Sergio", "Edad": 41, "Curso": "DAW1", "Grupo": "A", "Ciudad": "Albacete",     "Nota": 9.8, "Becado": True,  "Creditos": 66, "FechaMatricula": "2024-09-08"},
    {"ID": 9, "Nombre": "Nuria",  "Edad": 19, "Curso": "DAW2", "Grupo": "B", "Ciudad": "Puertollano", "Nota": 7.9, "Becado": True,  "Creditos": 62, "FechaMatricula": "2024-09-16"},
    {"ID":10, "Nombre": "Javier", "Edad": 52, "Curso": "DAW1", "Grupo": "C", "Ciudad": "Toledo",       "Nota": 4.9, "Becado": False, "Creditos": 48, "FechaMatricula": "2024-09-14"},
]

df = pd.DataFrame(data)
df2 = pd.DataFrame(datos)

# #filtrar por indice
# print(df.iloc[0])
# print('******************')
# #saca del 0 al 2
# print(df.iloc[:2])
# print('******************')
# print(df)
# print('******************')
# print(df.iloc[0,2])
# print('******************')
# print(df['Nombre'])
# print('******************')
# print(df['Edad'].mean())
# print('******************')
# print(df.sort_values('Nombre', ascending=False))
# print('******************')
# print(df[df['Edad'] >= 23 & (df['Edad'] <= 30)])
# print('******************')
# print(df[df['Mayor'] == True])
# print('******************')

#nota mayor que 5
print(df2[df2['Nota'] >= 5])
print('**************************')
#nombres de los alumnos becados
print(df2.loc[df2['Becado'] == True, 'Nombre'])
print('**************************')
#alumnos que sean de la ciudad de Puertollano y muestra solo su Nombre y Nota.
print(df2.loc[df2['Ciudad'] == 'Puertollano', ['Nombre', 'Nota']])
print('**************************')
#alumnos cuya Edad esté entre 20 y 40 años, ambos incluidos.
print(df2[(df2['Edad'] >= 20) & (df2['Edad'] <= 40)])
print('**************************')
#Top 3 de alumnos con mejor nota, mostrando Nombre, Curso y Nota.
print(df2.nlargest(3, 'Nota')[['Nombre', 'Curso', 'Nota']])
print('**************************')
#alumnos de DAW2 que además tengan Nota superior a 8
print(df2.loc[(df2['Nota'] > 8) & (df2['Curso'] == 'DAW2')])
print('**************************')
#todos los alumnos que NO están becados
print(df2[df2['Becado'] == False])
print('**************************')
#alumnos cuya Fecha de matrícula sea posterior al 12 de septiembre de 2024
df2['FechaMatricula'] = pd.to_datetime(df2['FechaMatricula'], format="%Y-%m-%d")
print(df2.loc[df2['FechaMatricula'] > "2024-09-12"])