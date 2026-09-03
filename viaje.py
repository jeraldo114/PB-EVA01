class Viaje:


    def __init__(self, id, origen, destino):

        self.id = id
        self.origen = origen
        self.destino = destino
        self.distancia = 0.0
        self.tarifa = 0
        self.estado = "PENDIENTE"

    # IMPLEMENTAR metodo
    def calcularTarifa(self) -> int:
        # Regla de negocio 1: Tarifa base de $1.500 más $800 por km. 
        # Debe expresarse como número entero.
        self.tarifa = int(1500 + (800 * self.distancia))
        return self.tarifa