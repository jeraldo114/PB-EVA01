class Pago:
    def __init__(self, id: int, monto: int, metodo: str, estado: str):
        self.id = id
        self.monto = monto
        self.metodo = metodo
        self.estado = estado

    def obtenerMonto(self) -> int:
        return self.monto

    def generarComprobante(self) -> None:
        # Según el UML, retorna void. Imprimimos el comprobante por consola.
        print("\n--- COMPROBANTE DE PAGO ---")
        print(f"ID Transacción : {self.id}")
        print(f"Monto Pagado   : ${self.monto}")
        print(f"Método de Pago : {self.metodo}")
        print(f"Estado         : {self.estado}")
        print("---------------------------\n") 