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

class ErrorCriticoLog(ErrorSistema):
    """Se dispara si el sistema de archivos falla"""
    def __init__(self, mensaje="No se pudo escribir en el archivo de logs"):
        super().__init__(mensaje)