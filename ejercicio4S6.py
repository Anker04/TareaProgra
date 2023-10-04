class Reserva:
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha):
        self.nombre_del_pasajero = nombre_del_pasajero
        self.numero_de_vuelo = numero_de_vuelo
        self.fecha = fecha

    def mostrar_detalle(self):
        return f"Reserva para {self.nombre_del_pasajero}\nNúmero de Vuelo: {self.numero_de_vuelo}\nFecha: {self.fecha}"

class ReservaEconomica(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, asiento):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.asiento = asiento

    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}\nClase: Económica\nAsiento: {self.asiento}"

class ReservaBusiness(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, lounge_access):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.lounge_access = lounge_access

    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}\nClase: Business\nAcceso a Sala VIP: {self.lounge_access}"

class ReservaPrimeraClase(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, servicio_chauffeur):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.servicio_chauffeur = servicio_chauffeur

    def mostrar_detalle(self):
        detalle_padre = super().mostrar_detalle()
        return f"{detalle_padre}\nClase: Primera Clase\nServicio de Chauffeur: {self.servicio_chauffeur}"

# Ejemplo de uso:
reserva_economica = ReservaEconomica("Juan Pérez", "AA123", "2023-10-15", "25B")
reserva_business = ReservaBusiness("María Gómez", "BA456", "2023-10-20", True)
reserva_primera_clase = ReservaPrimeraClase("Carlos Rodriguez", "LH789", "2023-10-25", True)

print("Detalles de la Reserva Económica:")
print(reserva_economica.mostrar_detalle())

print("\nDetalles de la Reserva Business:")
print(reserva_business.mostrar_detalle())

print("\nDetalles de la Reserva de Primera Clase:")
print(reserva_primera_clase.mostrar_detalle())
