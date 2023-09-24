"""
Crea una clase base llamada Personaje con los siguientes atributos y métodos:
    Atributos: nombre, nivel, vida
    Método __init__ para inicializar estos atributos.
    Método atacar que simula un ataque del personaje y muestra un mensaje genérico.
Crea dos clases derivadas: Guerrero y Mago.

Guerrero debe tener los siguientes atributos y métodos adicionales:
    Atributos: fuerza, defensa
    Método atacar que muestra un mensaje específico para el guerrero y calcula el daño del ataque basado en la fuerza y la defensa.
Mago debe tener los siguientes atributos y métodos adicionales:
    Atributos: poder, energia
    Método atacar que muestra un mensaje específico para el mago y calcula el daño del ataque basado en el poder y la energía.

Crea una clase Equipo que pueda contener varios personajes (guerreros y magos).
    Debe tener un método agregar_personaje para agregar un personaje al equipo.
    Debe tener un método ataque_total que calcule y muestre el daño total infligido por todo el equipo en un ataque coordinado.

Crea varios personajes (al menos un guerrero y un mago) y agrégalos a un equipo.
Realiza una serie de ataques para probar la lógica de combate del juego y muestra el daño total infligido por el equipo.
"""

class Personaje: 
    def __init__(self, nombre: str, nivel: int, vida: int):
        self.nombre = nombre
        self.nivel = nivel 
        self.vida = vida

    
class Guerrero(Personaje):
    def __init__(self, nombre: str, nivel: int, vida: int, fuerza: int, defensa: int):
        super().__init__(nombre, nivel, vida)
        self.fuerza = fuerza
        self.defensa = defensa
        self.calculo_danio = (self.fuerza + self.defensa) / 5.55

    def ataque(self):
        return "{} ({}) realizó un ataque que causó {}".format(self.nombre, self.nivel, self.calculo_danio)
    
class Mago(Personaje):
    def __init__(self, nombre: str, nivel: int, vida: int, poder: int, energia: int):
        super().__init__(nombre, nivel, vida)
        self.poder = poder
        self.energia = energia
        self.calculo_danio = (self.poder + self.energia) / 5.55

    def ataque(self):
        return "{} ({}) realizó un ataque que causó {}".format(self.nombre, self.nivel, self.calculo_danio)
    
class Equipo:
    def __init__(self):
        self.miembros = []

    def agregar_personaje(self, personaje: Personaje):
        self.miembros.append(personaje)
        return "El personaje {} se agregó con éxito".format(personaje.nombre)
    
    def ataque_total(self):
        total = 0
        for miembro in self.miembros:
            total += int(miembro.calculo_danio)
        return "El daño causado por el equipo es de {}".format(total)

#Agregamos guerrero
comandante = Guerrero("BarbaKahn", 18, 2000, 875, 500)
#Agregamos mago
mid = Guerrero("Ryze", 18, 1433, 1200, 150)
#Agregamos equipo
mi_equipo = Equipo()
mi_equipo.agregar_personaje(comandante)
mi_equipo.agregar_personaje(mid)
