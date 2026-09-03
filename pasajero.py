from persona import Persona
from viaje import Viaje


class Pasajero(Persona):

    def __init__(self, id, nombre, email, telefono, metodoPago, calificacionPromedio=0.0):

        super().__init__(id, nombre, email, telefono)

        self.metodoPago = metodoPago
        self.calificacionPromedio = calificacionPromedio

    def solicitarViaje(self, origen, destino):

        if origen == destino:
            print("Error: el origen y el destino no pueden ser iguales.")
            return None

        viaje = Viaje(origen, destino)

        return viaje

    def cancelarViaje(self, viaje):

        if viaje.estado == "PENDIENTE" or viaje.estado == "ACEPTADO":
            viaje.estado = "CANCELADO"
            return True

        print("Error: el viaje no puede ser cancelado.")
        return False

    # IMPLEMENTAR METODO
    def calificarViaje(self, viaje: Viaje, puntuacion: int) -> bool:
        
        # Validación 1: El estado debe ser "FINALIZADO".
        if viaje.estado != "FINALIZADO":
            print("Error: El viaje no se encuentra FINALIZADO.")
            return False
            
        # Validación 2: Puntuación entre 1 y 5.
        if puntuacion < 1 or puntuacion > 5:
            print("Error: La puntuación debe estar entre 1 y 5.")
            return False
            
        # Si ambas validaciones pasan.
        print(f"Calificación exitosa: {puntuacion} estrellas registradas.")
        return True