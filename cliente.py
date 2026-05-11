class Cliente:
    """
    Representa a un cliente dentro del sistema Software FJ.
    
    Esta clase gestiona la información personal del cliente, aplicando 
    encapsulamiento y validaciones de datos de entrada.
    """
    
    def __init__(self, nombre, cedula, email):


        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        if not cedula.isdigit():
            raise ValueError("La cédula debe contener solo números")

        if "@" not in email:
            raise ValueError("Correo electrónico inválido")

        self.__nombre = nombre
        self.__cedula = cedula
        self.__email = email


    def get_nombre(self):
        return self.__nombre
    """Retorna el nombre del cliente."""

    def get_cedula(self):
        return self.__cedula
    """Retorna la cédula del cliente."""


    def get_email(self):
        return self.__email
    """Retorna el email del cliente."""

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | CC: {self.__cedula} | Email: {self.__email}"
    
    def validar_dominio_email(self):
        
        """Verifica que el email pertenezca a dominios permitidos."""
        dominios_validos = ["gmail.com", "outlook.com", "unad.edu.co"]
        dominio = self.__email.split("@")[-1]
        if dominio not in dominios_validos:
            # Esto genera un registro de advertencia sin romper el programa
            return f"Advertencia: El dominio {dominio} no es corporativo."
        return "Dominio verificado."
