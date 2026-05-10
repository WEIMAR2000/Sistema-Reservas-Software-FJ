from abc import ABC, abstractmethod


# Clase abstracta
class Servicio(ABC):

    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base


    @abstractmethod
    def calcular_costo(self):
        pass


    @abstractmethod
    def descripcion(self):
        pass



# Servicio de reserva de salas
class ReservaSala(Servicio):

    def __init__(self, horas):
        super().__init__("Reserva de Sala", 50000)
        self.horas = horas


    def calcular_costo(self):
        return self.precio_base * self.horas


    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"



# Servicio de alquiler de equipos
class AlquilerEquipo(Servicio):

    def __init__(self, dias):
        super().__init__("Alquiler de Equipo", 30000)
        self.dias = dias


    def calcular_costo(self):
        return self.precio_base * self.dias


    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"



# Servicio de asesoría especializada
class AsesoriaEspecializada(Servicio):

    def __init__(self, horas):
        super().__init__("Asesoría Especializada", 80000)
        self.horas = horas


    def calcular_costo(self):
        return self.precio_base * self.horas


    def descripcion(self):
        return f"Asesoría especializada por {self.horas} horas"
    
    
