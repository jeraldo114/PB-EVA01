class Persona:
    def __init__(self, id: int, nombre: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def iniciarSesion(self) -> bool:
        return True

    # Realizar este metodo para actualizar el telefono de la persona.
    def actualizarTelefono(self, telefono: str) -> None:
        self.telefono = telefono

    def obtenerNombre(self) -> str:
        return self.nombre