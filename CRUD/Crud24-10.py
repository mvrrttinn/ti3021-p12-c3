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
personas = []

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
    for persona in personas:
         print("="*20)
         print(persona)
         print("="*20)


def update_persona():
    rut_busqueda = int(input("Ingrese el rut de la persona sin digito verificador: "))
    for persona in personas:
        if persona.rut == rut_busqueda:
             while True:
                    print(f"""
                           ~~~~~~~~~~~~~~~~~~~
                         ||Edicion de Personas||
                           ~~~~~~~~~~~~~~~~~~~
                         1. Rut: {persona.rut}
                         2. Digito verificador: {persona.digito_verificador}
                         3. Nombre: {persona.nombre}
                         4. Apellidos: {persona.apellido}
                         5. Fecha de nacimiento: {persona.fecha_nacimiento}
                         6. Codigo de area: {persona.cod_area}
                         7. Telefono: {persona.telefono}
                         0. No seguir modificando
                         """
                        )
                    opc = input("Ingrese una opcion a modificar: ")
                    if opc == "1":
                       rut: int = int(input("Ingresa el rut de la persona: "))
                       for persona in personas:
                            if persona.rut == rut:
                                 print(f"La persona con el rut {persona.rut} ya existe, Intente con otro rut.")
                            else:
                                 persona.rut = rut 
                                 print("Rut modificado exitosamente.")
                    elif opc == "2":
                       digito_verificador: str = input("Ingrese el digito verificador: ")
                       persona.digito_verificador = digito_verificador
                       print("Digito verificador modificado exitosamente.")
                    elif opc == "3":
                       nombre: str = input("Ingresa nombre de la persona: ")
                       persona.nombre = nombre
                       print("Nombre modificado exitosamente.")
                    elif opc == "4":
                       apellido: str = input("Ingresa apellido de la persona: ")
                       persona.apellido = apellido
                       print("Nombre modificado exitosamente.")   
                    elif opc == "5":
                     dia_nacimiento = int(input("Ingreas el dia de nacimiento de la persona: ")) 
                     mes_nacimiento = int(input("Ingreas el mes de nacimiento de la persona: "))
                     anio_nacimiento = int(input("Ingreas el año de nacimiento de la persona: "))
                     fecha_nacimiento: date = date(
                         year = anio_nacimiento,
                         month = mes_nacimiento,
                         day = dia_nacimiento
                     )
                     persona.fecha_nacimiento = fecha_nacimiento
                     print("Fecha de nacimiento modificado exitosamente")
                    elif opc == "6":
                         cod_area: int = int(input("Ingresa el codigo de area del telefono de la persona: ")) 
                         persona.cod_area = cod_area
                         print("Codigo de area modificado exitosamente.")
                    elif opc == "7":
                         telefono: int = int(input("Ingresar el numero de telefono de la persona: "))
                         persona.telefono = telefono 
                         print("Telefono modificado exitosamente.")
                    elif opc == "0":
                         print("Saliendo....")
                         break          

                    else:
                         print("Opcion invalida.")
                         input("Presione ENTER para continuar...")
    print(f"Persona con rut {rut_busqueda}, no encontrada.")
    input("Presione ENTER para continuar...")                         


def delete_persona():
      rut_busqueda = int(input("Ingresa el rut sin digito verificador: "))
      for persona in personas:
           if rut_busqueda == persona.rut:
                print(f"Eliminando persona con datos {persona}")
                personas.remove(persona)
                print(f"persona con rut {rut_busqueda} eliminada exitosamente")

      print(f"Persona con rut {rut_busqueda}, no encontrada.")
      input("Presiona ENTER para continuar")          




def menu():
     while True:
          print("""
                 1. Ver persona existente.
                 2. Crear persona
                 3. Leer personas
                 4. Actualizar persona
                 5. Eliminar persona
                 6. Salir
                """)
          opc = int(input("Ingrese una opcion: "))
          if opc == "1":
               persona_existe()
          elif opc == "2":
               create_persona()
          elif opc == "3":
               read_persona()
          elif opc == "4":
               update_persona()
          elif opc == "5":
               delete_persona()
          elif opc == "6":
               print("Saliendo...")
               break     
          else:
               print("Opcion no valida.")
               input("Presione ENTER para continuar.")
menu()               

               
               
