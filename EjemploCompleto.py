from abc import ABC, abstractmethod
from datetime import date

# ==============================
# Clase Cliente
# ==============================
class Cliente:
    def __init__(self, id: int, nombre: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def obtener_nombre(self) -> str:
        return self.nombre

    def obtener_telefono(self) -> str:
        return self.telefono


# ==============================
# Clase Boleta
# ==============================
class Boleta:
    def __init__(self, pedido_id: int, fecha: date, total: int):
        self.pedido_id = pedido_id
        self.fecha = fecha
        self.total = total

    def muestra(self, registro: str) -> str:
        return f"{registro}: Pedido #{self.pedido_id} - Fecha: {self.fecha} - Total: ${self.total}"


# ==============================
# Clase abstracta Pedido
# ==============================
class Pedido(ABC):
    def __init__(self, id: int, fecha: date, total: int, cliente: Cliente):
        self.id = id
        self.fecha = fecha
        self.total = total
        self.cliente = cliente

    @abstractmethod
    def procesar(self) -> Boleta:
        pass


# ==============================
# Subclases de Pedido
# ==============================
class PedidoADomicilio(Pedido):
    def __init__(self, id: int, fecha: date, total: int, cliente: Cliente,
                 direccion_entrega: str, nombre_repartidor: str, nombre_receptor: str):
        super().__init__(id, fecha, total, cliente)
        self.direccion_entrega = direccion_entrega
        self.nombre_repartidor = nombre_repartidor
        self.nombre_receptor = nombre_receptor

    def procesar(self) -> Boleta:
        print(f"Procesando pedido a domicilio para {self.cliente.obtener_nombre()}...")
        return Boleta(self.id, self.fecha, self.total)


class PedidoLocal(Pedido):
    def __init__(self, id: int, fecha: date, total: int, cliente: Cliente, numero_mesa: int):
        super().__init__(id, fecha, total, cliente)
        self.numero_mesa = numero_mesa

    def procesar(self) -> Boleta:
        print(f"Procesando pedido local en mesa {self.numero_mesa} para {self.cliente.obtener_nombre()}...")
        return Boleta(self.id, self.fecha, self.total)


class PedidoRetiro(Pedido):
    def __init__(self, id: int, fecha: date, total: int, cliente: Cliente, tiempo_estimado_retiro: date):
        super().__init__(id, fecha, total, cliente)
        self.tiempo_estimado_retiro = tiempo_estimado_retiro

    def procesar(self) -> Boleta:
        print(f"Procesando pedido para retiro de {self.cliente.obtener_nombre()}...")
        return Boleta(self.id, self.fecha, self.total)


# ==============================
# Clase Restaurante
# ==============================
class Restaurante:
    def __init__(self):
        self.pedidos: list['Pedido'] = []

    def registrar_pedido(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)
        print(f"Pedido registrado del cliente: {pedido.cliente.obtener_nombre()}")

    def calcular_total(self) -> int:
        return sum(p.total for p in self.pedidos)

    def lista_pedidos(self) -> list:
        return self.pedidos


# ==============================
# Ejemplo de uso
# ==============================
if __name__ == "__main__":
    c1 = Cliente(1, "Juan", "987654321")
    c2 = Cliente(2, "María", "912345678")

    r = Restaurante()

    p1 = PedidoLocal(101, date.today(), 20000, c1, 5)
    p2 = PedidoADomicilio(102, date.today(), 15000, c2, "Calle Falsa 123", "Carlos", "María")
    p3 = PedidoRetiro(103, date.today(), 18000, c1, date.today())

    for pedido in [p1, p2, p3]:
        r.registrar_pedido(pedido)
        boleta = pedido.procesar()
        print(boleta.muestra("Registro"))

    print(f"Total ventas del día: ${r.calcular_total()}")
