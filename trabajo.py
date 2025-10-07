#Definir calses

class Cliente():
    def __init__(self, id: str, nombre: str, telefono: int):
        self._id:str= id
        self._nombre:str= nombre
        self._telefono:int= telefono



class restaurante():
    def __init__(self, id:str, nombre:str, direccion:str):
        self._id:str = id
        self.nombre:str = nombre
        self.direccion:str = direccion
        self._clientes: list[Cliente] = []
            def classmethod registrar_pedido(cls):
            return f"El cliente {self._clientes._nombre} ha registrado un pedido"
            {self._clientes._nombre}

        def classmethod calcular_total(cls):
            return f"El total del pedido es de {pedido._total}" 


class pedido():
   def __init__(self, id: str, fecha: str, total: float, cliente: Cliente):
        self._id:str = id
        self._fecha:str = fecha
        self._total:float = total
        self._cliente:Cliente = cliente 

class pedido_domicilio():
    def __init__(self, cliente: Cliente):
        self._clientes.append(Cliente)
        return f"El cliente {cliente._nombre} ha pedido un domicilio"

class pedido_local():
    def __init__(self, cliente: Cliente):
        self._clientes.append(Cliente)
        return f"El cliente {cliente._nombre} ha pedido en el local"

class pedido_retiro():
    def __init__(self, cliente: Cliente):
        self._clientes.append(Cliente)
        return f"El cliente {cliente._nombre} ha pedido para retiro"
    