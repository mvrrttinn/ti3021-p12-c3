class Participante:
    def __init__(self, rut: str, nombre: str, edad: int):
        self._rut: str = rut
        self._nombre: str = nombre
        self._edad: int = edad
        
    def presentarse(self) -> str:
        return f"Hola mi nombre es {self._nombre} y mi edad es {self._edad}"
    
    def __str__(self):
        return "Me estas usando como string"

participante1: Participante = Participante("22208963-8","Martin Tapia", 19)

print(participante1.presentarse())


