"""
Ejercicio: Sistema de Gestión de Empleados

Imagina que estás construyendo un sistema de gestión de empleados para una empresa. Los empleados pueden ser de dos tipos diferentes: 
trabajadores a tiempo completo y trabajadores a tiempo parcial. Además, la empresa quiere tener una lista de todos los empleados ordenados 
por su salario de manera eficiente utilizando el algoritmo QuickSort.

Debes crear las siguientes clases:

-Empleado: Una clase base que tiene los atributos comunes a todos los empleados, como nombre y salario. 
          También, implementa un método __str__ que muestra la información básica del empleado.

-EmpleadoTiempoCompleto: Una subclase de Empleado que agrega atributos específicos para empleados a tiempo completo, 
                        como bono anual y horas extra. Debes implementar un método calcular_salario_total que calcule el salario total 
                        teniendo en cuenta el salario base, el bono anual y las horas extras.

-EmpleadoTiempoParcial: Una subclase de Empleado que agrega atributos específicos para empleados a tiempo parcial, como tarifa por hora 
                       y horas trabajadas. Debes implementar un método calcular_salario_total que calcule el salario total teniendo en 
                       cuenta la tarifa por hora y las horas trabajadas.

-ListaEmpleados: Una clase que tiene una lista de empleados y puede ordenarlos por salario 
                utilizando el algoritmo QuickSort. Debe tener un método agregar_empleado para 
                agregar empleados a la lista y un método ordenar_por_salario para ordenar la lista de empleados por salario.
"""

import random

class Empleado:
    def __init__(self, nombre: str, salario_bruto: float, cargo: str):
        self.nombre = nombre 
        self.salario_bruto = salario_bruto 
        self.cargo = cargo
    def __str__(self):
        return '{} - {}, salario: {}'.format(self.nombre, self.cargo, self.salario_bruto)
    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, salario_bruto: float, cargo: str, horas_extras: int):
        super().__init__(nombre, salario_bruto, cargo)
        self.bonoAnual = ((salario_bruto * 12) * 0.15) / 12 #15% del salario anual / 12 (pago de bono mensual)
        self.seguridad_social = salario_bruto * 0.0945 # 9.45% seguridad social
        self.horas_extras = horas_extras

    def salario_neto(self):
        return (self.salario_bruto + self.bonoAnual + (self.horas_extras * (self.salario_bruto / 40)) - self.seguridad_social)
    
class EmpleadoTiempoParcial(Empleado): #Freelancer
    def __init__(self, nombre: str, cargo: str, tarifa_hora: int, horas_por_mes: int, salario_bruto=None):
        super().__init__(nombre, salario_bruto, cargo)
        self.tarifa_hora = tarifa_hora
        self.horas_por_mes = horas_por_mes
        self.salario_bruto = self.tarifa_hora * self.horas_por_mes

    def salario_mensual(self, incentivo_productividad):
        return self.salario_bruto + incentivo_productividad
    
class ListaEmpleados:
    def __init__(self):
        self.lista_empleados = []
        self.salarios = []
        self.nombres = []
        self.jsonOrdenado = {}

    def contratar(self, empleado: Empleado):
        self.salarios.append(empleado.salario_bruto)
        self.nombres.append(empleado.nombre)
        self.lista_empleados.append(empleado)
        return "Se agregó al empleado {}, desempeñará el cargo de {}".format(empleado.nombre, empleado.cargo)
    
    def empleados_salarios(self):
        def particionado(salarios, nombres, menor, mayor):
            pivote_salarios = salarios[menor] #pivote = al primer elemento de la lista de salarios
            izq = menor + 1
            der = mayor

            while True:
                
                while izq <= der and salarios[izq] <= pivote_salarios: #comparamos al cursor izquierdo(segundo elemento de la lista) con el pivote
                    izq += 1   #Si el puntero izquierdo es menor o igual que el pivote, repetimos el proceso con el siguiente elemento

                while izq <= der and salarios[der] >= pivote_salarios: #comparamos al cursor derecho(último elemento de la lista) con el pivote
                    der -= 1 #Si el puntero derecho es mayor o igual que el pivote, repetimos el proceso con el siguiente elemento

                if der < izq: #verificamos que el puntero derecho no sea menor que el izquierdo, es decir que [5,9,1,DERECHO,IZQUIERDO,6,4,8]
                    break #Si esto pasa, quiere decir que hemos divido la lista principal en dos listas y podemos aplicar recursividad
                else: 
                    salarios[izq], salarios[der], nombres[izq], nombres[der] = salarios[der], salarios[izq], nombres[der], nombres[izq] #Cambiamos los elementos de la lista de lugar para continuar el ordenamiento
            
            salarios[menor], salarios[der], nombres[menor], nombres[der] = salarios[der], salarios[menor], nombres[der], nombres[menor] #El pivote es la actual frontera entre los menores y los mayores, por lo que lo ubicamos en la mitad de la lista [cursor derecho]
            return der 


        def quicksort(salarios, nombres, menor, mayor): #Parametros: la lista a ordenar, el primer elemento de la lista[0], el último elemento de la lista(len(lista)-1)
            if menor < mayor: #La lista tiene más de un elemento, por lo que no sabemos si está ordenada
                pivote = particionado(salarios, nombres, menor, mayor) #Obtenemos la frontera entre los menores y los mayores [der]
                quicksort(salarios, nombres, menor, pivote-1) 
                quicksort(salarios, nombres, pivote+1, mayor) #Aplicamos recursividad, la función se ejecutará n(logn) veces, dividiendo la lista log(n) veces
        quicksort(self.salarios, self.nombres, 0, len(self.salarios)-1)
        for i in range(0, len(self.salarios)):
            self.jsonOrdenado[self.nombres[i]] = self.salarios[i]
        return self.jsonOrdenado


#Crear gestión de empleados
mis_empleados = ListaEmpleados()


for i in range(100):
    nombre = f"Empleado{i+1}"  # Nombre default 'Empleado'
    salario = random.randint(1000, 2000)  # Salario aleatorio entre 1000 y 2000
    puesto = f"Puesto{i+1}"  # Puesto default 'Puesto'
    empleado = EmpleadoTiempoCompleto(nombre, salario, puesto, 0)  # Ajusta según el tipo de empleado
    mis_empleados.contratar(empleado)

for i in range(100):
    nombre = f"Freelancer{i+1}"  # Nombre default 'Empleado'
    tarifa_hora = random.randint(7, 20)  # Salario aleatorio entre 1000 y 2000
    horas_por_mes = random.randint(60, 90)  # Salario aleatorio entre 1000 y 2000
    puesto = f"Puesto{i+1}"  # Puesto default 'Puesto'
    empleado = EmpleadoTiempoParcial(nombre, puesto, tarifa_hora, horas_por_mes)  # Ajusta según el tipo de empleado
    mis_empleados.contratar(empleado)


print(mis_empleados.empleados_salarios())