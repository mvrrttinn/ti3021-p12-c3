import oracledb
import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

with oracledb.connect(
    user=username,
    password=password,
    dsn=dsn
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
            "CREATE TABLE CLIENTE ("
            "id INTERGER PRIMARY KEY UNIQUE,"
            "nombre VARCHAR(200),"
            "telefono VARCHAR(12)"
            ")"
        ),
        (

            "CREATE TABLE RESTAURANTE ("
            "id INTEGER PRIMARY KEY"
            "Direccion VARCHAR(30)"
            ")"
        ),
        (

            "CREATE TABLE PEDIDO ("
            "id INTERGER PRIMARY KEY,"
            "fecha DATETIME,"
            "total INTERGER,"
            "id_clienteFK INTERGER,"
            "FOREIGN KEY id_clienteFK REFERENCES CLIENTE(id)"
            "id_pedidoFK INTERGER,"
            "FOREIGN KEY id_pedidoFK references PEDIDO(id)"
            ")"
        ),
        (
            "CREATE TABLE PEDIDO_LOCAL ("
            "id INTEGER PRIMARY KEY"
            "numeroMesa INTERGER"
            "id_pedidoFK INTERGER,"
            "FOREIGN KEY id_pedidoFK references PEDIDO(id)"
            ")"
        ),
        (
            "CREATE TABLE PEDIDO_DOMICILIO ("
            "id INTEGER PRIMARY KEY"
            "direccionEntrega VARCHAR(100),"
            "nombreRepartidor VARCHAR(20)"
            "nombreReceptor VARCHAR(20)"
            "id_pedidoFK INTERGER,"
            "FOREIGN KEY id_pedidoFK references PEDIDO(id)"
            ")"
        ),
        (
            "CREATE TABLE PEDIDO_RETIRO ("
            "id INTEGER PRIMARY KEY"
            "tiempoEstimadoRetiro TIME"
            "id_pedidoFK INTERGER,"
            "FOREIGN KEY id_pedidoFK references PEDIDO(id)"
            ")"
        ),
        (
            "CREATE TABLE BOLETA ("
            "id INERGER PRIMARY KEY,"
            "fecha DATETIME,"
            "id_pedidoFK INTERGER,"
            "total INTERGER;"
            "FOREIGN KEY id_pedidoFK references PEDIDO(id)"
            ")"

        )
    ]
    for query in tables:
        create_schema(query)


def create_cliente(
    id,
    nombre,
    telefono
):
    pass


def create_restaurant(
       id,
       direccion
):
    pass


def create_pedido(
    id,
    fecha,
    total,
    idCliente,
    idPedido

):
    pass


def create_pedido_local(
       id,
       numeroMesa,
       idPedido
):
    pass


def create_pedido_domicilio(
    id,    
    direccionEntrega,
    nombreRepartidor,
    nombreReceptor,
    idPedido
):
    pass


def create_pedido_retiro(
    id,
    tiempoEstimadoRetiro,
    idPedido
):
    pass


def create_boleta(
    id,
    fecha,
    idPedido,
    total
):
    pass
