from datetime import datetime
from time import strftime

# Dado el archivo Libro2.xlsx contiene 21 nombres (ofuscados) y datos personales de una carga masiva de usuarios en nuestra aplicación
# Tenemos que realizar un programa en python que lea los datos proporcionados en un .txt y escriba un fichero con los inserts que realizaremos en la BBDD.
# Nuestras columnas en la BBDD son Nombre, Apellidos, fecha_nacimiento, calle, codigo_postal, numero, movil.
# Ejemplo de insert:
# Insert into Personas (id,Nombre, Apellidos, fecha_nacimiento, calle, codigo_postal, numero, movil) values (seq_personas.nextval("personas_seq", "Francisco", "Alia", "04/05/1992","Falsa","123","+34666666666");
#
# El fichero si no existe debe crearse con la fecha actual + Personas.log. Ejemplo:
# "12092025_Personas.log"

fecha = datetime.now().strftime("%d%m%y").lower()
log_name = fecha + "_Personas.log"

with open(log_name, "w") as l:
    
