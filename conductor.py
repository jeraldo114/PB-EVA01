from persona import Persona
from viaje import Viaje
from vehiculo import Vehiculo

class Conductor(Persona):
    def __init__(self, id: int, nombre: str, email: str, telefono: str, licencia: str, vehiculo: Vehiculo, calificacionPromedio: float = 0.0):
        super().__init__(id, nombre, email, telefono)
        self.licencia = licencia
        self.disponible = True
        self.calificacionPromedio = calificacionPromedio
        self.viajesRealizados = []
        self.vehiculo = vehiculo

    def aceptarViaje(self, viaje: Viaje) -> bool:
        if not self.disponible:
            print("Error: el conductor no está disponible.")
            return False
        if viaje.estado != "PENDIENTE":
            print("Error: el viaje no está pendiente.")
            return False
        viaje.estado = "ACEPTADO"
        self.disponible = False
        return True

    def rechazarViaje(self, viaje: Viaje) -> bool:
        if viaje.estado != "PENDIENTE":
            print("Error: solo se pueden rechazar viajes pendientes.")
            return False
        viaje.estado = "CANCELADO"
        return True

    # Método implementado y corregido según UML
    def cambiarDisponibilidad(self, disponible: bool) -> None:
        self.disponible = disponible

    def obtenerHistorial(self) -> list:
        return self.viajesRealizados