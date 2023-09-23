"""
Crea una clase llamada Libro que tenga los siguientes atributos:
-titulo (una cadena de texto)
-autor (una cadena de texto)
-anio_publicacion (un entero)
-disponible (un booleano que indica si el libro está disponible para ser prestado o no)

Luego, crea una clase llamada Biblioteca que tenga los siguientes métodos:
-__init__(self): Inicializa una lista vacía para almacenar los libros.
-agregar_libro(self, libro): Recibe un objeto Libro y lo agrega a la lista de libros de la biblioteca.
-prestar_libro(self, titulo): Recibe el título de un libro y cambia su estado a no disponible si está en la biblioteca. Si el libro no está en la biblioteca o ya está prestado, muestra un mensaje de error.
-devolver_libro(self, titulo): Recibe el título de un libro y cambia su estado a disponible si está en la biblioteca y estaba prestado. Si el libro no está en la biblioteca o ya está disponible, muestra un mensaje de error.
-listar_libros_disponibles(self): Muestra una lista de todos los libros disponibles en la biblioteca.
A continuación, crea algunos objetos Libro y una instancia de Biblioteca, agrega los libros a la biblioteca y realiza algunas operaciones de préstamo y devolución.
"""

class Libro:
    def __init__(self, titulo: str, autor: str, anio_publicacion: int, disponible: bool):
        self.titulo = titulo 
        self.autor = autor 
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible


class Biblioteca:
    def __init__(self):
        self.lista = []
    
    def agregar_libro(self, libro):
        self.lista.append(libro)
    
    def prestar_libro(self, titulo):
        for libro in self.lista:
            if libro.titulo == titulo:
                if libro.disponible == True:
                    libro.disponible = False
                else:
                    return {"error":"El libro no se encuentra disponible actualmente"}
    
    def devolver_libro(self, titulo):
        for libro in self.lista:
            if libro.titulo == titulo:
                libro.disponible = True
    
    def listar_libro_disponibles(self):
        disponibilidad = []
        for libro in self.lista:
            if libro.disponible == True: 
                disponibilidad.append(libro)
        return disponibilidad

libro1 = Libro("libro1", "david", 2023, True)
libro2 = Libro("libro2", "david", 2022, True)
libro3 = Libro("libro3", "david", 2021, False)
libro4 = Libro("libro4", "david", 2020, True)

MiBiblioteca = Biblioteca()
MiBiblioteca.agregar_libro(libro1)
MiBiblioteca.agregar_libro(libro2)
MiBiblioteca.agregar_libro(libro3)
MiBiblioteca.agregar_libro(libro4)
MiBiblioteca.prestar_libro("libro1")
MiBiblioteca.devolver_libro("libro1")

for disponible in MiBiblioteca.listar_libro_disponibles():
    print(disponible.titulo)

