class Vehiculo:
    def __init__(self, patente: str, marca: str, modelo: str, año: int, capacidad: int, estado: str):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad = capacidad
        self.estado = estado

    def obtenerInformacion(self) -> None:
        # Retorna void según UML, por lo que imprimimos directamente.
        print(f"--- Información del Vehículo ---")
        print(f"Patente   : {self.patente}")
        print(f"Marca     : {self.marca}")
        print(f"Modelo    : {self.modelo}")
        print(f"Año       : {self.año}")
        print(f"Capacidad : {self.capacidad} pasajeros")
        print(f"Estado    : {self.estado}")
        print("--------------------------------")

    def cambiarEstado(self, estado: str) -> None:
        self.estado = estado