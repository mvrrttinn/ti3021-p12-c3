
#Definir calses

class Cliente:
    def __init__(self, id: int, nombre: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def obtener_nombre(self):
        return self.nombre

    def obtener_telefono(self):
        return self.telefono




class Restaurante:
    def __init__(self):
        self.pedidos: list[Pedido] = []

    def registrar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)
        print(f"Pedido registrado del cliente: {pedido.cliente.obtener_nombre()}")

    def calcular_total(self):
        return sum(p.total for p in self.pedidos)

    def lista_pedidos(self):
        return self.pedidos

#Libreria abc para clases abstractas
from abc import ABC, abstractmethod
from datetime import date

class Pedido(ABC):
    def __init__(self, id: int, fecha: date, total: int, cliente: Cliente):
        self.id = id
        self.fecha = fecha
        self.total = total
        self.cliente = cliente

    @abstractmethod
    def procesar(self):
        pass


class PedidoADomicilio(Pedido):
    def __init__(self, id: int, fecha: date, total: int, cliente: Cliente,
                 direccion_entrega: str, nombre_repartidor: str, nombre_receptor: str):
        super().__init__(id, fecha, total, cliente)
        self.direccion_entrega = direccion_entrega
        self.nombre_repartidor = nombre_repartidor
        self.nombre_receptor = nombre_receptor

    def procesar(self):
        return Boleta(self.id, self.fecha, self.total)

class PedidoLocal(Pedido):
    def __init__(self, id: int, fecha: date, total: int, cliente: Cliente, numero_mesa: int):
        super().__init__(id, fecha, total, cliente)
        self.numero_mesa = numero_mesa

    def procesar(self):
        return Boleta(self.id, self.fecha, self.total)

class PedidoRetiro(Pedido):
    def __init__(self, id: int, fecha: date, total: int, cliente: Cliente, tiempo_estimado_retiro: date):
        super().__init__(id, fecha, total, cliente)
        self.tiempo_estimado_retiro = tiempo_estimado_retiro

    def procesar(self):
        return Boleta(self.id, self.fecha, self.total)

class Boleta:
    def __init__(self, pedido_id: int, fecha: date, total: int):
        self.pedido_id = pedido_id
        self.fecha = fecha
        self.total = total

    def muestra(self, registro: str):
        return f"{registro}: Pedido #{self.pedido_id} - Fecha: {self.fecha} - Total: ${self.total}"

#Ejemplo de uso