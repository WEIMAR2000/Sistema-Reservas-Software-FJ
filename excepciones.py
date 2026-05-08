# Excepción general del sistema
class ErrorSistema(Exception):

    def __init__(self, mensaje):
        super().__init__(mensaje)



# Excepción para clientes inválidos
class ErrorCliente(ErrorSistema):

    def __init__(self, mensaje):
        super().__init__(mensaje)



# Excepción para servicios inválidos
class ErrorServicio(ErrorSistema):

    def __init__(self, mensaje):
        super().__init__(mensaje)



# Excepción para reservas inválidas
class ErrorReserva(ErrorSistema):

    def __init__(self, mensaje):
        super().__init__(mensaje)
