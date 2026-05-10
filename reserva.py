from datetime import datetime


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"


    def confirmar(self):

        try:
            costo = self.servicio.calcular_costo()

            self.estado = "Confirmada"

            self.registrar_log(
                f"Reserva confirmada para {self.cliente.get_nombre()} | Total: ${costo}"
            )

            return f"Reserva confirmada. Total a pagar: ${costo}"

        except Exception as e:

            self.registrar_log(f"ERROR al confirmar reserva: {str(e)}")

            return "No se pudo confirmar la reserva"


    def cancelar(self):

        self.estado = "Cancelada"

        self.registrar_log(
            f"Reserva cancelada para {self.cliente.get_nombre()}"
        )

        return "Reserva cancelada correctamente"


    def mostrar_reserva(self):

        return (
            f"Cliente: {self.cliente.get_nombre()}\n"
            f"Servicio: {self.servicio.descripcion()}\n"
            f"Estado: {self.estado}"
        )
        
    def calcular_iva(self, tasa=0.19):
        try:
            costo_base = self.servicio.calcular_costo()
            return costo_base * tasa
        except Exception as e:
            self.registrar_log(f"Error al calcular IVA: {e}")
            return 0  


    def registrar_log(self, mensaje):

        with open("logs.txt", "a", encoding="utf-8") as archivo:

            fecha = datetime.now()

            archivo.write(f"[{fecha}] {mensaje}\n")
            
