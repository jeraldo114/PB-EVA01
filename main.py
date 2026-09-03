from pasajero import Pasajero
from conductor import Conductor
from vehiculo import Vehiculo
from pago import Pago
from viaje import Viaje 

def main():
    # En esta sección se instancian los objetos principales del sistema.
    # Se crean 2 pasajeros, 2 vehículos y 2 conductores según lo pedido en el pdf.
    
    # Crear pasajeros.
    pasajero1 = Pasajero(1, "Juan Perez", "juan@mail.com", "+56911111111", "Tarjeta", 5.0)
    pasajero2 = Pasajero(2, "Maria Silva", "maria@mail.com", "+56922222222", "Efectivo", 4.8)

    # Crear vehículos.
    vehiculo1 = Vehiculo("ABCD12", "Toyota", "Yaris", 2020, 4, "Operativo")
    vehiculo2 = Vehiculo("WXYZ98", "Nissan", "Versa", 2022, 4, "Operativo")

    # Crear conductores y asociarlos a los vehículos (Solicitado en la rúbrica).
    conductor1 = Conductor(3, "Pedro Diaz", "pedro@mail.com", "+56933333333", "Clase B", True, 4.9)
    conductor1.vehiculo = vehiculo1 # Hace una asociación directa.
    
    conductor2 = Conductor(4, "Luis Soto", "luis@mail.com", "+56944444444", "Clase B", True, 4.7)
    conductor2.vehiculo = vehiculo2 # Lo mismo, hace la asociación directa.

    # Actualizar teléfono (Uso de método heredado de la clase padre Persona).
    print(f"Teléfono antiguo de {pasajero1.obtenerNombre()}: {pasajero1.telefono}")
    pasajero1.actualizarTelefono("+56999999999")
    print(f"Teléfono actualizado de {pasajero1.obtenerNombre()}: {pasajero1.telefono}\n")

    # Solicitar los viaje 
    viaje1 = pasajero1.solicitarViaje("Plaza de Armas", "Universidad")
    viaje2 = pasajero2.solicitarViaje("Mall", "Centro")
    viaje3 = pasajero1.solicitarViaje("Estación", "Aeropuerto")

    # 1. El viaje nace con estado "PENDIENTE". Al ser aceptado por el conductor, pasa a "ACEPTADO".
    # Conductor acepta.
    print("--- Proceso de Viaje 1 ---")
    conductor1.aceptarViaje(viaje1)
    conductor1.cambiarDisponibilidad(False) # El conductor se ocupa

    # Definir distancia (hace una simulación necesaria para el cálculo matemático).
    viaje1.distancia = 5.0

    # 2. La tarifa se calcula con base 1500 + (800 * distancia).
    # Calcular tarifa.
    viaje1.calcularTarifa()
    print(f"Tarifa calculada: ${viaje1.tarifa}")

    # Inicia el viaje:
    # 3. Se cambia el estado progresivamente. iniciar() lo pasa a "EN_CURSO".
    viaje1.iniciar()
    viaje1.obtenerEstado() # Método void según UML, debería imprimir "EN_CURSO".

    # Finalizar viaje:
    # 4. finalizar() lo pasa a "FINALIZADO", requisito obligatorio para poder calificarlo.
    viaje1.finalizar()
    viaje1.obtenerEstado() # Debería imprimir "FINALIZADO".
    
    # Liberamos al conductor.
    conductor1.cambiarDisponibilidad(True)

    # Mostrar información.
    print("\n--- Resumen Final ---")
    print("Estado del Viaje:", viaje1.estado)
    print("Tarifa del Viaje:", viaje1.tarifa)

    # Generar pago.
    pago1 = Pago(1, viaje1.tarifa, pasajero1.metodoPago, "PAGADO")
    print("Monto del pago (desde objeto Pago):", pago1.obtenerMonto())
    pago1.generarComprobante()

    # Calificar viaje:
    # 5. La calificación exige estado "FINALIZADO" y puntuación de 1 a 5.
    print("\n--- Calificación ---")
    pasajero1.calificarViaje(viaje1, 5) # Éxito esperado.
    
    # Pruebas para validar que la regla de negocio funciona (mostrará errores en la consola).
    print("Prueba de error (Viaje no finalizado):")
    pasajero2.calificarViaje(viaje2, 4) # viaje2 sigue en PENDIENTE.
    
    print("Prueba de error (Nota fuera de rango):")
    pasajero1.calificarViaje(viaje1, 7) # Nota inválida.

if __name__ == "__main__":
    main()

    # https://github.com/jeraldo114/PB-EVA01.git