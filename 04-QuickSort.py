def particionado(lista, menor, mayor):
    pivote = lista[menor] #pivote = al primer elemento de la lista
    izq = menor + 1
    der = mayor

    while True:
        
        while izq <= der and lista[izq] <= pivote: #comparamos al cursor izquierdo(segundo elemento de la lista) con el pivote
            izq += 1   #Si el puntero izquierdo es menor o igual que el pivote, está bien y avanzamos 

        while izq <= der and lista[der] >= pivote: #comparamos al cursor derecho(último elemento de la lista) con el pivote
            der -= 1 #Si el puntero derecho es mayor o igual que el pivote, está bien y avanzamos 

        if der < izq: #verificamos que el puntero derecho no sea menor que el izquierdo, es decir que [5,9,1,DERECHO,IZQUIERDO,6,4,8]
            break #Si esto pasa, quiere decir que hemos divido la lista principal en dos listas y podemos aplicar recursividad
        else: 
            lista[izq], lista[der] = lista[der], lista[izq] #Cambiamos los elementos de la lista de lugar para continuar el ordenamiento
    
    lista[menor], lista[der] = lista[der], lista[menor] #El pivote es la actual frontera entre los menores y los mayores, por lo que lo ubicamos en la mitad de la lista [cursor derecho]
    return der 


def quicksort(lista, menor, mayor): #Parametros: la lista a ordenar, el primer elemento de la lista[0], el último elemento de la lista(len(lista)-1)
    if menor < mayor: #La lista tiene más de un elemento, por lo que no sabemos si está ordenada
        pivote = particionado(lista, menor, mayor) #Obtenemos la frontera entre los menores y los mayores [der]
        quicksort(lista, menor, pivote-1) 
        quicksort(lista, pivote+1, mayor) #Aplicamos recursividad, la función se ejecutará n(logn) veces, dividiendo la lista log(n) veces


lista = [3, -2, 0, 5, -1, 3, 7, -4, 0, 9, -3, 2, 6, -2, 8, 1, -1, 4, 5, 7]

quicksort(lista, 0, len(lista)-1)

print(lista)