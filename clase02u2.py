#definir clase Restaurant
class Restaurant:
    def __init__(self,nombre: str):
        self.nombre: str = nombre
        self.pedido = []

    def registrar_pedido(self, pedido: 'Pedido'):
        self.pedido.append(pedido)
        print(f"Pedido {pedido.id} registrado para {pedido.cliente._nombre}")

    def mostrar_pedidos(self):
        for p in self.pedidos:
            print(f"Pedido: {p.id} - Cliente: {p.cliente._nombre} - Total: {p.total}")    

#definir clase Cliente
class Cliente:
    def __init__(self, nombre: str, rut: str, correo: str):
        self._nombre: str = nombre
        self.__rut: str = rut
        self.__correo: str = correo

#definir clases Pedido
from datetime import datetime

class Pedido:
    def __init__(self, id: int, fecha: datetime, total: float, cliente: 'Cliente'):
        self.__id: int  = id
        self._fecha: datetime = fecha
        self._total: float = total
        self._cliente: 'Cliente' = cliente
    def mostrar_resumen(self):
        print(f"Pedido {self.id} de {self.cliente._nombre} por ${self.total}")

class PedidoADomicilio:
    def __init__(self, direccion: str, nombreRepartidor: str, nombreReceptor: str):
        self.__direccion: str = direccion
        self._nombreRepartidor: str = nombreRepartidor
        self._nombreReceptor: str = nombreReceptor

class PedidoLocal:
    def __init__(self,id: int , numeroMesa: int):
        self._id: int = id
        self._numeroMesa: int = numeroMesa

class PedidoRetiro:
    def __init__(self, id: int,tiempoEstimado: datetime):
        self._id: int = id
        self._tiempoEstimado: datetime = tiempoEstimado

#definir clase Boleta
class Boleta:
    def __init__(self, pedido: 'Pedido', fecha: datetime, total: float):
        self._pedido: 'Pedido' = pedido
        self._fecha: datetime = fecha
        self._total: float = total

#Crear Cliente
cliente1 = Cliente("Martin", "22208963-8", "martin.tapia16@inacapmail.cl")
#Crear Pedido
pedido1 = Pedido(1, datetime.now(), 15000, cliente1)
#Craer Boleta
boleta1 = Boleta(pedido1, datetime.now(), pedido1._total)
#Crear restaurante y registrar pedido
resto = Restaurant("FastBox Express")
resto.registrar_pedido(pedido1)
#Mostrar pedidos registrados
resto.mostrar_pedidos()
