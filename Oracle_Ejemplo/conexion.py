import oracledb
import os 
from dotenv import load_dotenv  
load_dotenv()  

username = os.getenv("ORACLE_USER") 
dsn = os.getenv("ORACLE_DSN") 
password = os.getenv("ORACLE_PASSWORD")  

with oracledb.connect(
user= username, 
password= password, 
dsn= dsn
) as connection:
       with connection.cursor() as cursor:         
              sql = "select sysdate from dual"         
              for row in cursor.execute(sql):
                     for column in row:             
                            print(column) 

def get_connection():
       return oracledb.connect(iuser=username, password=password, dsn=dsn)                            

def create_schema(query):
       try:
              with get_connection() as connection:
                     with connection.cursor() as cursor:
                            cursor.execute(query)
                            print(f"Tabla creada \n {query}")
       except oracledb.DatabaseError as error:
              print(f"No se pudo crear la tabla: {error}")                     
       
       tables = [
              (
                     "CREATE TABLE"
                     "CLIENTE ("
                     "id INTERGER PRIMARY KEY,"
                     "nombre VARCHAR(200),"
                     "telefono VARCHAR(12)"
                     ");"
              ),       
              (

                     "CREATE TABLE"
                     "RESTAURANTE ("
                     "Direccion VARCHAR(30)"
                     ");"
              ),
              (       

                     "CREATE TABLE"
                     "PEDIDO ("
                     "id INTERGER PRIMARY KEY,"
                     "fecha DATETIME,"
                     "total INTERGER,"
                     "id_clienteFK INTERGER,"
                     "FOREIGN KEY id_clienteFK REFERENCES CLIENTE(id)"
                     ");"
              )
              (       
                     "CREATE TABLE"
                     "PEDIDO_LOCAL ("
                     "numeroMesa INTERGER"
                     ");"
              )
              (
                     "CREATE TABLE"
                     "PEDIDO_DOMICILIO ("
                     "direccionEntrega VARCHAR(100),"
                     "nombreRepartidor VARCHAR(20)"
                     "nombreReceptor VARCHAR(20)"
                     ");"
              )
              (
                     "CREATE TABLE"
                     "PEDIDO_RETIRO ("
                     "tiempoEstimadoRetiro TIME"
                     ");"
              )
              (
                     "CREATE TABLE"
                     "BOLETA ("
                     "fecha DATETIME,"
                     "id_pedidoFK INTERGER,"
                     "total INTERGER;"
                     "FOREIGN KEY id_pedidoFK references PEDIDO(id)"
                     ");"

              )
       ]
for query in tables:
       create_schema(query)       