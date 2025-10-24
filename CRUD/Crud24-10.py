"""
Actividad practica y reflexion:
Implementa un sistema CRUD para al menos 3 clases distintas

CRUD
~~~~
Create: Crear un nuevo registro 
Read: Leer un registro/s
Update: Actualizar registro
Delete: Borrar registro
"""

"""
GLOSARIO
~~~~~~~~
Pass: Es la palabra reservada para que python no exijael codigo minimo,
para el funcionamiento de la funcion/metodo.

°IDE
Viene de la palavra integrated development eviroment,
que significa entorno de desarrollo integrado, que son los editores
de codigo que normalmente utilizamos para programar en la informatica.

°Lint o Linter
Es el encargado de vifilar la sintaxis del
codigo en el IDE sea cprrecta y te sugiere
el funcionamiento de este 

"""
#Importar libreria DATETIME
from datetime import date 


#Primero, debemos de crear una clase
class Persona:
    #Definir como se inicializa 
    def __init__(
            self,
            rut: int,
            digito_verificador: str,
            nombres: str,
            apellidos: str,
            fecha_nacimiento: date,
            cod_area: int,
            telefono: int 
    ):
            self.rut: int = rut
            self.digito_verificador: str = digito_verificador
            self.nombre: str = nombres
            self.apellido: str = apellidos
            self.fecha_nacimiento: date = fecha_nacimiento
            self.cod_area: int = cod_area
            self.telefono: int = telefono

# Lista para almacenar varios objetos intanciados en la clase persona 
personas: list[Persona] = []

def persona_existe(nueva_persona: Persona) -> bool:
      for persona in personas:
            if persona.rut == nueva_persona.rut:
                  print(f"Persona ya existe con rut: {persona.rut}-{persona.digito_verificador}")
                  return True
      


def create_persona():
    rut: int = int(input("Ingrese rut sindigito verificador: "))
    digito_verificador: str = input("Ingrese digito verificador: ")
    nombres: str = input("Ingrese nombre de la persona: ")
    apellidos: str = input("Ingrese apellido de la persona: ")
    dia_nacimiento: int = int(input("Ingrese el dia de nacimiento: "))
    mes_nacimiento: int = int(input("Ingrese el mes de nacimiento: "))
    anio_nacimiento: int = int(input("Ingrese el año de nacimiento: "))
    fecha_nacimiento: date = date(year = anio_nacimiento, month = mes_nacimiento, day = dia_nacimiento)
    cod_area: int = int(input("Ingrese codigo de area del numero de telefono: "))
    telefono: int = int(input("Ingrese numero de telefono sin codigo de area: "))

    nueva_persona = Persona(
            rut,
            digito_verificador,
            nombres,
            apellidos,
            fecha_nacimiento,
            cod_area,
            telefono
    )

    if persona_existe(nueva_persona):
        return print("No se registro la persona.")   
    else:
        personas.append(nueva_persona)

def read_persona():
    pass
def update_persona():
    pass
def delete_persona():            
      pass
      

create_persona()
print(personas)