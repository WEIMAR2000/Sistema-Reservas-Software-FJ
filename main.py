from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ErrorCliente, ErrorReserva


print("========== SISTEMA SOFTWARE FJ ==========\n")


# FUNCIÓN PARA REGISTRAR ERRORES
def registrar_error(error):

    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(str(error) + "\n")



# SIMULACIÓN 1
try:

    cliente1 = Cliente("Juan Pérez", "12345", "juan@gmail.com")

    servicio1 = ReservaSala(2)

    reserva1 = Reserva(cliente1, servicio1, 2)

    print(reserva1.confirmar())

except Exception as e:

    registrar_error(e)

    print("Error en simulación 1")



# SIMULACIÓN 2
try:

    cliente2 = Cliente("", "99999", "correo@gmail.com")

except Exception as e:

    registrar_error(e)

    print("Error: cliente inválido")



# SIMULACIÓN 3
try:

    cliente3 = Cliente("María", "abc", "maria@gmail.com")

except Exception as e:

    registrar_error(e)

    print("Error: cédula inválida")



# SIMULACIÓN 4
try:

    cliente4 = Cliente("Pedro", "77777", "correo_invalido")

except Exception as e:

    registrar_error(e)

    print("Error: email inválido")



# SIMULACIÓN 5
try:

    cliente5 = Cliente("Laura", "55555", "laura@gmail.com")

    servicio5 = AlquilerEquipo(5)

    reserva5 = Reserva(cliente5, servicio5, 5)

    print(reserva5.confirmar())

except Exception as e:

    registrar_error(e)

    print("Error en simulación 5")



# SIMULACIÓN 6
try:

    cliente6 = Cliente("Carlos", "44444", "carlos@gmail.com")

    servicio6 = AsesoriaEspecializada(3)

    reserva6 = Reserva(cliente6, servicio6, 3)

    print(reserva6.confirmar())

except Exception as e:

    registrar_error(e)

    print("Error en simulación 6")



# SIMULACIÓN 7
try:

    cliente7 = Cliente("Ana", "88888", "ana@gmail.com")

    servicio7 = ReservaSala(4)

    reserva7 = Reserva(cliente7, servicio7, -1)

    print(reserva7.confirmar())

except Exception as e:

    registrar_error(e)

    print("Error: duración inválida")



# SIMULACIÓN 8
try:

    cliente8 = Cliente("Miguel", "22222", "miguel@gmail.com")

    servicio8 = AlquilerEquipo(2)

    reserva8 = Reserva(cliente8, servicio8, 2)

    print(reserva8.cancelar())

except Exception as e:

    registrar_error(e)

    print("Error en simulación 8")



# SIMULACIÓN 9
try:

    cliente9 = Cliente("Sofía", "11111", "sofia@gmail.com")

    servicio9 = AsesoriaEspecializada(1)

    reserva9 = Reserva(cliente9, servicio9, 1)

    print(reserva9.mostrar_reserva())

except Exception as e:

    registrar_error(e)

    print("Error en simulación 9")



# SIMULACIÓN 10
try:

    cliente10 = Cliente("Andrés", "33333", "andres@gmail.com")

    servicio10 = ReservaSala(6)

    reserva10 = Reserva(cliente10, servicio10, 6)

    print(reserva10.confirmar())

except Exception as e:

    registrar_error(e)

    print("Error en simulación 10")


print("\n========== FIN DEL SISTEMA ==========")
