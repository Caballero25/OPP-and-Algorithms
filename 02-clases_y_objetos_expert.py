"""Crea un sistema de gestión de reservas de vuelos utilizando programación orientada a objetos en Python. Debes diseñar las siguientes clases:

Aeropuerto: Representa un aeropuerto con un nombre y una ubicación. Debe tener un método para mostrar información sobre el aeropuerto.

Vuelo: Representa un vuelo entre dos aeropuertos. Debe tener información sobre la aerolínea, número de vuelo, hora de salida, hora de llegada 
       y número de asientos disponibles. Debe permitir realizar reservas de asientos.

Pasajero: Representa a un pasajero con un nombre, número de pasaporte y una lista de vuelos reservados.

SistemaReservas: Esta clase debe gestionar todos los vuelos disponibles, los pasajeros y las reservas. Debe tener métodos para:
    -Mostrar una lista de todos los vuelos disponibles.
    -Permitir a un pasajero buscar vuelos por origen y destino, así como por fechas.
    -Reservar un asiento en un vuelo para un pasajero.
    -Mostrar las reservas de un pasajero en particular.
    -Mostrar todos los pasajeros en un vuelo en particular.
"""
#Clase constructura de aeropuertos 
class Aeropuerto:
    def __init__(self, nombre: str, ubicacion: str):
        self.nombre = nombre 
        self.ubicacion = ubicacion 
    def info(self):
        return f"Aeropuerto: {self.nombre} | Ubicación: {self.ubicacion}"

#Clase constructura de vuelos 
class Vuelo:
    def __init__(self, aerolinea: str, nvuelo: int, hrsalida: str, hrllegada: str, fecha_salida, fecha_llegada,
                 asientos_disponibles: int, origen: object, destino: object):
        self.aerolinea = aerolinea
        self.nvuelo = nvuelo
        self.hrsalida = hrsalida
        self.hrllegada = hrllegada
        self.fecha_salida = fecha_salida
        self.fecha_llegada = fecha_llegada
        self.asientos_disponibles = asientos_disponibles
        self.origen = origen 
        self.destino = destino
        self.reservas = {}

    def reservar_asientos(self, numero_de_asientos, pasajero):
        if self.asientos_disponibles >= numero_de_asientos:
            self.asientos_disponibles = self.asientos_disponibles - numero_de_asientos
            if pasajero in self.reservas:
                self.reservas[pasajero] += numero_de_asientos
            else:        
                self.reservas[pasajero] = numero_de_asientos
            return f"Realizó la reserva de {numero_de_asientos} asientos exitosamente"
        else: 
            return f"Error: fuera de rango. El número de asientos disponibles actualmente es de {self.asientos_disponibles}"

#Clase constructura de pasajeros 
class Pasajero:
    def __init__(self, nombres: str, npasaporte: int):
        self.nombres = nombres 
        self.npasaporte = npasaporte
        self.vuelos_reservados = {}

    def reservas(self):
        return self.vuelos_reservados

#Clase constructura de nuestro sistema 
class SistemaReservas(): 
    def __init__(self):
        self.aeropuertos = []
        self.vuelos = []
        self.pasajeros = []
    #Agregamos los datos existentes de las demás clases
    def agregar_aeropuerto(self, aeropuerto: object):
        self.aeropuertos.append(aeropuerto)
        return f"Se agregó con éxito la instancia {aeropuerto}"
    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)
        return f"Se agregó con éxito la instancia {vuelo}"
    def agregar_pasajero(self, pasajero: object):
        self.pasajeros.append(pasajero)
        return f"Se agregó con éxito la instancia {pasajero}"
    
    def vuelos_disponibles(self):
        return [vuelo for vuelo in self.vuelos if vuelo.asientos_disponibles >= 0]
    
    def buscar_vuelo(self, **kwargs):
        return [vuelo for vuelo in self.vuelos if vuelo.origen == kwargs.get("origen") or vuelo.destino == kwargs.get("destino") or vuelo.fecha_salida == kwargs.get("fecha_salida") or vuelo.fecha_llegada == kwargs.get("fecha_llegada")]

    def reservar_asiento(self, numero_de_asientos: int, vuelo: Vuelo, pasajero: Pasajero):
        pasajero.vuelos_reservados[f"De {vuelo.origen} a {vuelo.destino}"] = f"Salida el {vuelo.fecha_salida} - {vuelo.hrsalida}"
        return vuelo.reservar_asientos(numero_de_asientos, pasajero) 
    def pasajeros_vuelo(self, vuelo: Vuelo):
        return vuelo.reservas


#Registrar SistemaReservas
MiSistema = SistemaReservas()

#Registrar Aeropuertos
AeropuertoQuito = Aeropuerto("Ruminaui", "Quito")
AeropuertoMiami = Aeropuerto("Miami AIR", "Miami")
MiSistema.agregar_aeropuerto(AeropuertoQuito) #Agregamos nuestros objetos al sistema
MiSistema.agregar_aeropuerto(AeropuertoMiami) #Agregamos nuestros objetos al sistema 

#Registrar Pasajeros
pasajero1 = Pasajero("David Caballero", 123456)
MiSistema.agregar_pasajero(pasajero1) #Agregamos nuestros objetos al sistema
pasajero2 = Pasajero("Andres Mejía", 789456)
MiSistema.agregar_pasajero(pasajero2) #Agregamos nuestros objetos al sistema

#Registrar Vuelos
vueloMiamiEcuador = Vuelo("Avianca", 400, "17:00", "02:00", "23/9", "24/9", 50, AeropuertoQuito, AeropuertoMiami)
MiSistema.agregar_vuelo(vueloMiamiEcuador) #Agregamos nuestros objetos al sistema

MiSistema.reservar_asiento(10, vueloMiamiEcuador, pasajero1)
MiSistema.reservar_asiento(15, vueloMiamiEcuador, pasajero2)
