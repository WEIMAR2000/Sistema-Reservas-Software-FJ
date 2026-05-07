class Cliente:

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


    def get_cedula(self):
        return self.__cedula


    def get_email(self):
        return self.__email


    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | CC: {self.__cedula} | Email: {self.__email}"
